from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants
from otreeutils.pages import ExtendedPage



class Outro(ExtendedPage):
    form_model = models.Player
    form_fields = ['password']

class SurA(ExtendedPage):
    form_model = models.Player
    form_fields = ['risk','selfhidden','selfmatrices','selfmath']
    timeout_warning_seconds = 60
    timeout_warning_message = 'Bitte beeilen Sie sich, die Zeit ist um.'
    def before_next_page(self):
        self.player.set_total_payoff()

class SurB(ExtendedPage):
    form_model = models.Player
    form_fields = ['age', 'gen', 'eng', 'stud','com','joy']
    timeout_warning_seconds = 120
    timeout_warning_message = 'Bitte beeilen Sie sich, die Zeit ist um.'

class Outro2(ExtendedPage):
    pass

class Wait1(WaitPage):
    pass

class Wait2(WaitPage):
    pass


page_sequence = [
    SurA,
    Wait1,
    SurB,
    Wait2,
    Outro,
    Outro2
]
