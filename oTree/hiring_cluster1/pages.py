from otree.api import Currency as c, currency_range
from otreeutils.pages import ExtendedPage
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class Intro (Page):
    pass

class Payoffvorstellung1 (Page):
    timeout_seconds = 420

class Payoffvorstellung1X(ExtendedPage):
    timeout_warning_seconds = 1
    timeout_warning_message = 'Bitte beeilen Sie sich, die Zeit ist um.'


class Dec1(ExtendedPage):
    timeout_warning_seconds = 30
    timeout_warning_message = 'Bitte beeilen Sie sich, die Zeit ist um.'
    form_model = models.Player
    form_fields = ['diagonal']


class Indif1(ExtendedPage):
    timeout_warning_seconds = 30
    timeout_warning_message = 'Bitte beeilen Sie sich, die Zeit ist um.'
    form_model = models.Player
    form_fields = ['indif1']

class BeliefSlider(ExtendedPage):
    timeout_warning_seconds = 120
    timeout_warning_message = 'Bitte beeilen Sie sich, die Zeit ist um.'
    form_model = models.Player
    form_fields = ['offerone_0','offerone_1','offerone_2','offerone_3','offerone_4','offerone_5','offerone_6',
                   'offerone_7','offerone_8','offerone_9','offertwo_0','offertwo_1','offertwo_2','offertwo_3',
                   'offertwo_4','offertwo_5','offertwo_6','offertwo_7','offertwo_8','offertwo_9']

    def vars_for_template(self):
        return {'offer_numbers': range(0, 10),
                'price': [c(0.1),c(0.2),c(0.3),c(0.4),c(0.5),c(0.6),c(0.7),c(0.8),c(0.9),c(1.0)]}

class BeliefScale(ExtendedPage):
    timeout_warning_seconds = 60
    timeout_warning_message = 'Bitte beeilen Sie sich, die Zeit ist um.'
    form_model = models.Player
    form_fields = ['beliefscale1', 'beliefscale2']

class Payoffvorstellung2 (Page):
    timeout_seconds = 30
    def before_next_page(self):
        self.player.set_payoffs1()

class Payoffvorstellung2X (ExtendedPage):
    timeout_warning_seconds = 1
    timeout_warning_message = 'Bitte beeilen Sie sich, die Zeit ist um.'


page_sequence = [
    Intro,
    Payoffvorstellung1,
    Payoffvorstellung1X,
    Dec1,
    Indif1,
    BeliefSlider,
    BeliefScale,
    Payoffvorstellung2,
    Payoffvorstellung2X,
]
