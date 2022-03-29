import urllib.parse

class Embed:
    def __init__(self, title, **kwargs) -> None:
        """
        Initialize the embed object.

        Parameters:
            title (str): The title of the embed.
            description (str): The description of the embed. (Max 340 characters)
            colour (str): The hex colour of the embed.
            url (str): The url of the embed.
        """

        description = kwargs.get("description", "")
        colour = kwargs.get("colour", "") or kwargs.get("color", "") or "ffffff"
        url = kwargs.get("url", "")

        if colour.startswith("#"):
            colour = colour[1:]

        self.hide_text = "||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||"
        self.base_url = "https://embed.rauf.wtf/?"
        self.params = {
            "title": title,
            "description": description,
            "color": colour,
            "redirect": url
        }

    def __str__(self) -> str:
        """
        Return the url of the embed.

        Returns:
            str: The url of the embed.
        """

        return self.generate_url(hide_url=True)

    def set_author(self, text) -> None:
        """
        Set the author of the embed.

        Parameters:
            text (str): The text of the author.
        """

        self.params["author"] = text

    def set_image(self, url) -> None:
        """
        Set the image of the embed.

        Parameters:
            url (str): The url of the image.
        """

        self.params["image"] = url

    def generate_url(self, *, hide_url=False) -> str:
        """
        Generate the url of the embed.

        Returns:
            str: The url of the embed.
        """

        for key in list(self.params.keys()):
            if self.params[key] == "" or self.params[key] is None:
                del self.params[key]

        if hide_url:
            return self.hide_text + " " + self.base_url + urllib.parse.urlencode(self.params)
        else:
            return self.base_url + urllib.parse.urlencode(self.params)