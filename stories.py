"""Madlibs Stories."""


class Story:
    """Madlibs story.

    To  make a story, pass a list of prompts, and the text
    of the template.

        >>> s = Story(["noun", "verb"],
        ...     "I love to {verb} a good {noun}.")

    To generate text from a story, pass in a dictionary-like thing
    of {prompt: answer, promp:answer):

        >>> ans = {"verb": "eat", "noun": "mango"}
        >>> s.generate(ans)
        'I love to eat a good mango.'
    """

    def __init__(self, title, words, text):
        """Create story with words and template text."""
        self.title = title
        self.prompts = words
        self.template = text

    def generate(self, answers):
        """Substitute answers into text."""

        text = self.template

        for (key, val) in answers.items():
            text = text.replace("{" + key + "}", val)

        return text

# Different stories

story_1 = Story(
    "Old tale",
    ["place", "noun", "verb", "adjective", "plural_noun"],
    "Once upon a time in a long-ago {place}, there lived a large {adjective} {noun}. It loved to {verb} {plural_noun}."
)

story_2 = Story(
    "Judgy",
    ["name", "verb", "adjective"],
    "{name} is really {adjective} when they {verb}."
)

story_3 = Story(
    "Rare Sighting",
    ["animal", "sound", "place"],
    "The {animal} went '{sound}' all the way to {place}."
)

stories = {

    "story1": story_1,
    "story2": story_2,
    "story3": story_3
}
