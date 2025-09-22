def banner_text(text: str = " ", screen_width: int = 80) -> None:
    """
    Prints out different lines of a banner created with `** on each sides`.

    :param text: Prints str inside the banner.
        An asterisk (*) will result in a row of asterisks.
        Prints out " " by default if left empty.
    :param screen_width: The width of the banner by character number.
        The width is set to 80 by default if left empty.
    :raises ValueError: if the supplied str is too long to fit the banner.
    :return:
        None
    """
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
banner_text("! ! ! EMERGENCY DISTRESS SIGNAL ! ! !", 60)
banner_text("FROM:", 60)
banner_text("Nepal, Tribhuvan International Airport", 60)
banner_text(screen_width = 60)
banner_text("Location: [Longitude, Latitude] NW 340°", 60)
banner_text("*", 60)

# We added default arguments for the str, and also learn to use keyword argument (line 16)
# Next time we will learn to document our functions before writing them
# This is helpful cus now you know what you are working towards
