"""profile creator in social networks
"""
from abc import ABC, abstractmethod
from typing import List


class Section(ABC):
    """abstract section
    """

    @abstractmethod
    def describe(self) -> str:
        """describe of section

        Returns:
            str: section description
        """

    @abstractmethod
    def attributes(self) -> list:
        """attributes of section

        Returns:
            list: list of section attributes
        """


class PersonalInfoSection(Section):
    """personal info section
    """

    def describe(self):
        return "Personal Information Section."

    def attributes(self):
        return ["name", "username", "email", "holding", "is_active"]


class AlbumSection(Section):
    """album section
    """

    def describe(self):
        return "Album Information Section."

    def attributes(self):
        return ["name", "tracks", "number_of_tracks", "views", "income"]


class ProjectSection(Section):
    """project section
    """

    def describe(self):
        return "Project Information Section."

    def attributes(self):
        return ["title", "date", "description", "files", "likes"]


class Profile(ABC):
    """abstract factory class
    """

    def __init__(self):
        self.sections: List[object] = []
        # creator method
        self.create_profile()

    @abstractmethod
    def create_profile(self):
        """create profile abstractmethod
        """

    def get_sections(self) -> List[object]:
        """get all sections

        Returns:
            List[object]: list of sections
        """
        return self.sections

    def add_section(self, new_section: object):
        """add section to sections list

        Args:
            new_section (object): section
        """
        self.sections.append(new_section)


class LinkedIn(Profile):
    """linkedin profile
    """

    def create_profile(self):
        self.add_section(PersonalInfoSection)
        self.add_section(ProjectSection)


class Spotify(Profile):
    """spotify profile
    """

    def create_profile(self):
        self.add_section(PersonalInfoSection)
        self.add_section(AlbumSection)


if __name__ == "__main__":
    choice_sections: dict = {
        "1": LinkedIn,
        "LinkedIn": LinkedIn,
        "2": Spotify,
        "Spotify": Spotify,
    }

    profile_input: str = input("Select Your Profile For Creation:"
                               "\n1-LinkedIn\n2-Spotify\n>>> ")
    profile: Profile = choice_sections[profile_input]()
    print(f"Your {profile.__class__.__name__} Profile Created!")
    all_sections = list(
        map(lambda section: section.__name__, profile.get_sections())
    )
    print("Your Sections =>", *all_sections)

    print("\nAbout Your Account Sections:")
    sections = profile.get_sections()
    for section in sections:
        this_section: Section = section()
        print(this_section.describe())
