from .constants import colors

def construct_styled_component(tag, index, input1, colored, input2):
    html = f"""
    <{tag}>
        {input1}
        <span style='background-color: {colors[index]}'>
            {colored}
        </span>
        {input2}
    </{tag}>
    """

    return html