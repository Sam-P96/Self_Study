def banner_text(text, screen_width=80):
    # screen_width = y # I originally used this, but you can just change it up there
    if len(text) > screen_width - 4:
        raise ValueError("String {0} is larger than specified width {1}"
                         .format(text, screen_width))
    if text == "*":
        print("*" * screen_width)
    else:
        output_string = f"**{text.center(screen_width - 4)}**"
        print(output_string)


banner_text("*")
banner_text("BITCH")
banner_text("I SAID WHAT I SAID something something paint the town red")
banner_text("something something instead...")
banner_text("*")

