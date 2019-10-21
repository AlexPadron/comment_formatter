from typing import List, Optional


def get_indentation_for_comment(line: str) -> int:
    """Get the number of spaces before a comment"""
    return len(line.split("#")[0])


def is_comment(line: str) -> bool:
    """True if a line is a comment, else False"""
    return line.strip().startswith("#")


def get_text_for_comment(line: str) -> Optional[str]:
    """Get the text of a comment"""
    stripped_line = line.lstrip()

    if stripped_line.startswith("#"):
        text = stripped_line[1:]

        # There are three cases here 1) The comment is only a # character (with optional spaces),
        # return None 2) The comment has a leading space, strip it 3) The comment does not have a
        # leading space
        if len(text) == 0 or all(x == " " for x in text):
            return None
        elif text.startswith(" ") and len(text) > 1:
            return text[1:]
        else:
            return text
    else:
        raise AssertionError("Cannot get text for a line that isn't a comment")


def get_words_in_comment(line: str) -> List[str]:
    """Get the words in a comment"""
    text = get_text_for_comment(line)

    if text is None:
        raise AssertionError("Cannot get words for an empty comment")
    else:
        return text.split(" ")


def add_line_to_block_lines(
    block_lines: List[str], current_line: List[str], indentation: int
) -> None:
    """Format the current line into a string and add it to block lines"""
    line_string = (" " * indentation) + "# " + " ".join(current_line)
    block_lines.append(line_string)


def rewrite_comments(source: str, max_line_length: int) -> str:
    """Rewrite the comments in a source file to be line length compliant"""
    source_lines = source.split("\n")
    rewritten_lines = []
    i = 0

    while i < len(source_lines):
        line = source_lines[i]
        # We do not want to reformat comment lines that are empty because these indicate paragraphs.
        #
        # As shown here, we want to treat this and the above as separate comment blocks
        if is_comment(line) and (get_text_for_comment(line) is not None):
            # If we land on a comment, we want to find all comments within the same block
            first_comment_index = i
            indentation = get_indentation_for_comment(line)
            last_comment_index = i

            while True:
                next_line = source_lines[last_comment_index + 1]
                # Comment blocks must have the same indentation. In the below snippet:
                #
                #  if foo:      pass      # Comment 1  # Comment 2
                #
                # Comment 1 and Comment 2 are not part of the same block
                if (
                    is_comment(next_line)
                    and (get_indentation_for_comment(next_line) == indentation)
                    and (get_text_for_comment(next_line) is not None)
                ):
                    last_comment_index += 1
                else:
                    break

            all_comment_words: List[str] = []

            for index in range(first_comment_index, last_comment_index + 1):
                all_comment_words += get_words_in_comment(source_lines[index])

            # Once we have collected all words in a block, format them into appropriate lines
            block_lines: List[str] = []
            current_line: List[str] = []
            current_line_length = 0

            for word in all_comment_words:
                # Add 2 because we are going to add in '# ' Add in the length of the spaces (=
                # len(current_line) - 1)
                if (
                    indentation
                    + 2
                    + len(word)
                    + current_line_length
                    + (len(current_line))
                ) <= max_line_length:
                    pass
                elif len(current_line) > 0:
                    # When a very long word cannot fit in a line by itself, do not add an empty line
                    # as a prefix
                    add_line_to_block_lines(block_lines, current_line, indentation)
                    current_line = []
                    current_line_length = 0
                else:
                    pass

                current_line.append(word)
                current_line_length += len(word)

            if current_line_length > 0:
                add_line_to_block_lines(block_lines, current_line, indentation)

            for line in block_lines:
                rewritten_lines.append(line)

            i += last_comment_index - first_comment_index + 1
        else:
            # If the line is not a comment, add it to the output without reformatting it
            rewritten_lines.append(line)
            i += 1

    return "\n".join(rewritten_lines)


def rewrite_file(
    file_name: str,
    check: bool,
    max_line_length: int = 100,
    output_file_name: Optional[str] = None,
) -> bool:
    """Rewrite a file to have comments with the correct length"""
    with open(file_name) as f:
        text = f.read()

    first_pass_text = rewrite_comments(text, max_line_length)
    second_pass_text = rewrite_comments(first_pass_text, max_line_length)

    if first_pass_text != second_pass_text:
        raise AssertionError(
            "First pass over text gave a different result from the second. "
            "This indicates an internal error, please file a bug report"
        )

    if check:
        return text == first_pass_text
    else:
        output_file_name = output_file_name or file_name

        with open(output_file_name, "w") as f:
            f.write(second_pass_text)

        return True
