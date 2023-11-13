from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

import random


from django.core.validators import (MaxValueValidator, MinValueValidator)

author = 'Stefan Gehrig'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'hiring_cluster4'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass

class Player(BasePlayer):
    password = models.CharField()
    age = models.IntegerField()

    gen = models.IntegerField(
        choices=[
            [1, 'Weiblich'],
            [2, 'Männlich'], ],
        widget=widgets.RadioSelect()
    )
    eng = models.IntegerField(
        choices=[
            [1, 'Ja'],
            [2, 'Nein'], ],
        widget=widgets.RadioSelect()
    )
    stud = models.CharField(max_length=100)
    joy = models.IntegerField(
        choices=[
            [1, 'Ja'],
            [2, 'Nein'], ],
        widget=widgets.RadioSelect()
    )

    com = models.CharField()

    risk = models.IntegerField(
    choices=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    widget=widgets.RadioSelectHorizontal
    )

    selfmath = models.PositiveIntegerField(validators=[MaxValueValidator(100)])
    selfhidden = models.PositiveIntegerField(validators=[MaxValueValidator(100)])
    selfmatrices = models.PositiveIntegerField(validators=[MaxValueValidator(100)])

    total_payoff = models.CurrencyField()
    payoffapp1 = models.CurrencyField()
    payoffapp1_1 = models.CurrencyField()
    payoffapp1_2 = models.CurrencyField()
    payoffapp23 = models.CurrencyField()
    total_payoff_plus_fee = models.CurrencyField()

    def set_total_payoff(self):

        self.payoffapp1 = self.participant.vars.get('p11') + self.participant.vars.get('p12')
        self.total_payoff = self.payoffapp1 + random.choice([self.participant.vars.get('p2'),self.participant.vars.get('p3'),
                                                                         self.participant.vars.get('p4'),self.participant.vars.get('p5'),
                                                                         self.participant.vars.get('p6'),self.participant.vars.get('p7'),
                                                                         self.participant.vars.get('p8'),self.participant.vars.get('p9')])
        self.total_payoff_plus_fee = self.total_payoff+(5)
        self.payoffapp23 = self.total_payoff - self.payoffapp1
        self.payoffapp1_1 = self.participant.vars.get('p11')
        self.payoffapp1_2 = self.participant.vars.get('p12')
        self.participant.payoff = self.total_payoff