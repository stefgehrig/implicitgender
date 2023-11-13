from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants
from otreeutils.pages import ExtendedPage


class Dec6(ExtendedPage):
    def is_displayed(self):
        return self.round_number == self.participant.vars['task_rounds']['A']
    timeout_warning_seconds = 30
    timeout_warning_message = 'Bitte beeilen Sie sich, die Zeit ist um.'
    form_model = models.Player
    form_fields = ['dec6']

class Indif6(ExtendedPage):
    def is_displayed(self):
        return self.round_number == self.participant.vars['task_rounds']['A']
    timeout_warning_seconds = 30
    timeout_warning_message = 'Bitte beeilen Sie sich, die Zeit ist um.'
    form_model = models.Player
    form_fields = ['indif6']
    def before_next_page(self):
        self.player.set_payoffs3()

class Dec7(ExtendedPage):
    def is_displayed(self):
        return self.round_number == self.participant.vars['task_rounds']['B']
    timeout_warning_seconds = 30
    timeout_warning_message = 'Bitte beeilen Sie sich, die Zeit ist um.'
    form_model = models.Player
    form_fields = ['dec7']

class Indif7(ExtendedPage):
    def is_displayed(self):
        return self.round_number == self.participant.vars['task_rounds']['B']
    timeout_warning_seconds = 30
    timeout_warning_message = 'Bitte beeilen Sie sich, die Zeit ist um.'
    form_model = models.Player
    form_fields = ['indif7']
    def before_next_page(self):
        self.player.set_payoffs3()

class Dec8(ExtendedPage):
    def is_displayed(self):
        return self.round_number == self.participant.vars['task_rounds']['C']
    timeout_warning_seconds = 30
    timeout_warning_message = 'Bitte beeilen Sie sich, die Zeit ist um.'
    form_model = models.Player
    form_fields = ['dec8']

class Indif8(ExtendedPage):
    def is_displayed(self):
        return self.round_number == self.participant.vars['task_rounds']['C']
    timeout_warning_seconds = 30
    timeout_warning_message = 'Bitte beeilen Sie sich, die Zeit ist um.'
    form_model = models.Player
    form_fields = ['indif8']
    def before_next_page(self):
        self.player.set_payoffs3()

class Dec9(ExtendedPage):
    def is_displayed(self):
        return self.round_number == self.participant.vars['task_rounds']['D']
    timeout_warning_seconds = 30
    timeout_warning_message = 'Bitte beeilen Sie sich, die Zeit ist um.'
    form_model = models.Player
    form_fields = ['dec9']

class Indif9(ExtendedPage):
    def is_displayed(self):
        return self.round_number == self.participant.vars['task_rounds']['D']
    timeout_warning_seconds = 30
    timeout_warning_message = 'Bitte beeilen Sie sich, die Zeit ist um.'
    form_model = models.Player
    form_fields = ['indif9']
    def before_next_page(self):
        self.player.set_payoffs3()





page_sequence = [
    Dec6,
    Indif6,
    Dec7,
    Indif7,
    Dec8,
    Indif8,
    Dec9,
    Indif9,
]
