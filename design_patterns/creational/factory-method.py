from abc import ABCMeta,	abstractmethod


class Profile(metaclass=ABCMeta):
    def init(self):
        self.sections = []
        self.create_profile()

    @abstractmethod
    def create_profile(self):
        pass

    def get_sections(self):
        return self.sections

    def add_sections(self,	section):
        self.sections.append(section)


class Linkedin(Profile):
    def create_profile(self):
        self.add_sections({'type': 'content', 'id': 'photo'})
        self.add_sections({'type': 'list', 'id': 'work_experience'})
        self.add_sections({'type': 'list', 'id': 'skills'})


class Facebook(Profile):
    def create_profile(self):
        self.add_sections({'type': 'content', 'id': 'photo'})
        self.add_sections({'type': 'list', 'id': 'posts'})


class ProfileFactory:
    def get_profile(self, profile):
        if profile == 'facebook':
            return Facebook()
        elif profile == 'linkedin':
            return Linkedin()
        else:
            raise ValueError(profile)
