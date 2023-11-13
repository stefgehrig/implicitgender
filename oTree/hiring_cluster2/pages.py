from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from otreeutils.pages import ExtendedPage
from .models import Constants


class Dec2(ExtendedPage):
    def is_displayed(self):
        return self.round_number == self.participant.vars['task_rounds']['A']
    timeout_warning_seconds = 30
    timeout_warning_message = 'Bitte beeilen Sie sich, die Zeit ist um.'
    form_model = models.Player
    form_fields = ['dec2']

class Indif2(ExtendedPage):
    def is_displayed(self):
        return self.round_number == self.participant.vars['task_rounds']['A']
    timeout_warning_seconds = 30
    timeout_warning_message = 'Bitte beeilen Sie sich, die Zeit ist um.'
    form_model = models.Player
    form_fields = ['indif2']
    def before_next_page(self):
        self.player.set_payoffs2()


class Dec3(ExtendedPage):
    def is_displayed(self):
        return self.round_number == self.participant.vars['task_rounds']['B']
    timeout_warning_seconds = 30
    timeout_warning_message = 'Bitte beeilen Sie sich, die Zeit ist um.'
    form_model = models.Player
    form_fields = ['dec3']

class Indif3(ExtendedPage):
    def is_displayed(self):
        return self.round_number == self.participant.vars['task_rounds']['B']
    timeout_warning_seconds = 30
    timeout_warning_message = 'Bitte beeilen Sie sich, die Zeit ist um.'
    form_model = models.Player
    form_fields = ['indif3']
    def before_next_page(self):
        self.player.set_payoffs2()

class Dec4(ExtendedPage):
    def is_displayed(self):
        return self.round_number == self.participant.vars['task_rounds']['C']
    timeout_warning_seconds = 30
    timeout_warning_message = 'Bitte beeilen Sie sich, die Zeit ist um.'
    form_model = models.Player
    form_fields = ['dec4']

class Indif4(ExtendedPage):
    def is_displayed(self):
        return self.round_number == self.participant.vars['task_rounds']['C']
    timeout_warning_seconds = 30
    timeout_warning_message = 'Bitte beeilen Sie sich, die Zeit ist um.'
    form_model = models.Player
    form_fields = ['indif4']
    def before_next_page(self):
        self.player.set_payoffs2()

class Dec5(ExtendedPage):
    def is_displayed(self):
        return self.round_number == self.participant.vars['task_rounds']['D']
    timeout_warning_seconds = 30
    timeout_warning_message = 'Bitte beeilen Sie sich, die Zeit ist um.'
    form_model = models.Player
    form_fields = ['dec5']

class Indif5(ExtendedPage):
    def is_displayed(self):
        return self.round_number == self.participant.vars['task_rounds']['D']
    timeout_warning_seconds = 30
    timeout_warning_message = 'Bitte beeilen Sie sich, die Zeit ist um.'
    form_model = models.Player
    form_fields = ['indif5']
    def before_next_page(self):
        self.player.set_payoffs2()

page_sequence = [
    Dec2,
    Indif2,
    Dec3,
    Indif3,
    Dec4,
    Indif4,
    Dec5,
    Indif5
]
