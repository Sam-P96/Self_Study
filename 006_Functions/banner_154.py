def banner_text(text = " ", screen_width = 80):
    # screen_width = y # I originally used this, but you can just change it up there
    if len(text) > screen_width - 4:
        raise ValueError("String {0} is larger than specified width {1}"
                         .format(text, screen_width))
    if text == "*":
        print("*" * screen_width)
    else:
        output_string = f"**{text.center(screen_width - 4)}**"
        print(output_string)


banner_text("*", 60)
banner_text("BITCH", 60)
banner_text("I SAID WHAT I SAID", 60)
banner_text(screen_width = 60)
banner_text("something something instead...", 60)
banner_text("*", 60)

# We added default arguments for the str, and also learn to use keyword argument (line 16)
# Next time we will learn to document our functions before writing them
# This is helpful cus now you know what you are working towards
