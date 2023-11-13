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
    name_in_url = 'hiring_cluster1'
    players_per_group = None
    num_rounds = 1
    incent_binary = (6)
    # certificates have been awarded with random tie breaking once for payoff calculation, and here are their performances
    male_all = [ 3, 3, 5, 3, 1, 2, 5, 3, 3, 4, 3, 5, 4, 6, 5, 6, 5, 3, 3, 5, 6, 3, 3, 1, 4, 4, 3, 2, 5, 6, 7, 4, 3, 7, 3, 5]
    female_all = [4, 4, 2, 4, 5, 5, 1, 3, 4, 3, 4, 6, 4, 4, 3, 2, 6, 5, 6, 4, 3, 4, 6, 1, 5, 4, 3, 7, 2, 4, 3, 4, 6, 4, 2, 5, 4, 4, 4, 4, 6, 4, 4, 6]
    candidates_all = [ 4, 3, 4, 2, 3, 4, 5, 5, 3, 5, 1, 1, 3, 4, 3, 2, 5, 3, 3, 4, 4, 6, 3, 4, 4, 5, 3, 4, 2, 6, 6, 5, 6,
                    5, 6, 4, 5, 3, 3, 4, 6, 1, 3, 5, 5, 4, 3, 7, 2, 4, 6, 3, 3, 3, 1, 4, 4, 6, 4, 3, 4, 2, 5, 2, 6, 5,
                    7, 4, 4, 4, 4, 4, 3, 6, 7, 3, 4, 5, 4, 6]

    male_certgk   = [ 3, 2, 3, 6, 5, 3, 5, 6, 3, 2, 6, 7, 4, 5 ]
    female_certgk = [4, 4, 6, 3, 6, 6, 4, 5, 4, 6 ]

    male_certhf   = [ 3, 5, 1, 3, 6, 6, 5, 3, 4, 5, 7 ]
    female_certhf = [4, 2, 4, 3, 6, 4, 1, 4, 4, 6, 4, 4, 4]

    certhf = [ 3, 5, 1, 3, 6, 6, 5, 3, 4, 5, 7, 4, 2, 4, 3, 6, 4, 1, 4, 4, 6, 4, 4, 4]
    certgk = [ 3, 2, 3, 6, 5, 3, 5, 6, 3, 2, 6, 7, 4, 5, 4, 4, 6, 3, 6, 6, 4, 5, 4, 6]

    binvec = [0,1]
    mediancutvec = [1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0]
    hunvec = [1,2,3,4,5,6,7,8,9,10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
            20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
            30, 31, 32, 33, 34, 35, 36, 37, 38, 39,
            40, 41, 42, 43, 44, 45, 46, 47, 48, 49,
            50, 51, 52, 53, 54, 55, 56, 57, 58, 59,
            60, 61, 62, 63, 64, 65, 66, 67, 68, 69,
            70, 71, 72, 73, 74, 75, 76, 77, 78, 79,
            80, 81, 82, 83, 84, 85, 86, 87, 88, 89,
            90, 91, 92, 93, 94, 95, 96, 97, 98, 99,
            100]


class Subsession(BaseSubsession):
    def creating_session(self):
        for player in self.get_players():
            player.treat = random.choice(['einsA', 'einsB', 'zweiA', 'zweiB'])

class Group(BaseGroup):
    pass

class Player(BasePlayer):

    diagonal = models.BooleanField()

    indif1 = models.BooleanField()

    beliefscale1 = models.IntegerField(
    choices=[1, 2, 3, 4, 5],
    widget=widgets.RadioSelectHorizontal
)
    beliefscale2 = models.IntegerField(
    choices=[1, 2, 3, 4, 5],
    widget=widgets.RadioSelectHorizontal
)

    treat = models.CharField()

    payoffdec1 = models.CurrencyField()

    payoffbelief = models.CurrencyField()
    beliefpayoff1 = models.CurrencyField()
    beliefpayoff2 = models.CurrencyField()

    offerone_0 = models.BooleanField()
    offerone_1 = models.BooleanField()
    offerone_2 = models.BooleanField()
    offerone_3 = models.BooleanField()
    offerone_4 = models.BooleanField()
    offerone_5 = models.BooleanField()
    offerone_6 = models.BooleanField()
    offerone_7 = models.BooleanField()
    offerone_8 = models.BooleanField()
    offerone_9 = models.BooleanField()

    offertwo_0 = models.BooleanField()
    offertwo_1 = models.BooleanField()
    offertwo_2 = models.BooleanField()
    offertwo_3 = models.BooleanField()
    offertwo_4 = models.BooleanField()
    offertwo_5 = models.BooleanField()
    offertwo_6 = models.BooleanField()
    offertwo_7 = models.BooleanField()
    offertwo_8 = models.BooleanField()
    offertwo_9 = models.BooleanField()

    numberdraw1 = models.IntegerField()
    numberdraw2 = models.IntegerField()

    pick11A = models.IntegerField()
    pick11B = models.IntegerField()
    pick12A = models.IntegerField()
    pick12B = models.IntegerField()
    pickbel1 = models.IntegerField()
    pickbel2 = models.IntegerField()

    def set_payoffs1(self):

        self.pick11A = random.choice(Constants.male_certgk)
        self.pick11B = random.choice(Constants.female_certhf)
        self.pick12A = random.choice(Constants.male_certhf)
        self.pick12B = random.choice(Constants.female_certgk)
        self.pickbel1 = random.choice(Constants.certgk)
        self.pickbel2 = random.choice(Constants.certhf)

        if self.treat == "einsA" or self.treat == "einsB":
            if self.indif1 == 0:
                if self.pick11A > self.pick11B and self.diagonal == 1:
                    self.payoffdec1 = Constants.incent_binary
                elif self.pick11A < self.pick11B and self.diagonal == 0:
                    self.payoffdec1 = Constants.incent_binary
                elif self.pick11A < self.pick11B and self.diagonal == 1:
                    self.payoffdec1 = 0
                elif self.pick11A > self.pick11B and self.diagonal == 0:
                    self.payoffdec1 = 0
                elif self.pick11A == self.pick11B:
                    self.payoffdec1 = Constants.incent_binary * random.choice(Constants.binvec)
            else:
                self.payoffdec1 = 0.1 + Constants.incent_binary * random.choice(Constants.binvec)
        else:
            if self.indif1 == 0:
                if self.pick12A > self.pick12B and self.diagonal == 1:
                    self.payoffdec1 = Constants.incent_binary
                elif self.pick12A < self.pick12B and self.diagonal == 0:
                    self.payoffdec1 = Constants.incent_binary
                elif self.pick12A < self.pick12B and self.diagonal == 1:
                    self.payoffdec1 = 0
                elif self.pick12A > self.pick12B and self.diagonal == 0:
                    self.payoffdec1 = 0
                elif self.pick12A == self.pick12B:
                    self.payoffdec1 = Constants.incent_binary * random.choice(Constants.binvec)
            else:
                self.payoffdec1 = 0.1 + Constants.incent_binary * random.choice(Constants.binvec)

        self.numberdraw1 = random.choice(range(0,10))

        if [self.offerone_0,self.offerone_1,self.offerone_2,self.offerone_3,
                      self.offerone_4,self.offerone_5,self.offerone_6,self.offerone_7,
                      self.offerone_8,self.offerone_9][self.numberdraw1] == 1:
            if self.pickbel1 > 4:
                self.beliefpayoff1 = 4 - self.numberdraw1/10
            elif self.pickbel1 == 4:
                self.beliefpayoff1 = 1 + random.choice(Constants.mediancutvec) * 3 - self.numberdraw1/10
            elif self.pickbel1 < 4:
                self.beliefpayoff1 = 1 - self.numberdraw1/10

        if [self.offerone_0,self.offerone_1,self.offerone_2,self.offerone_3,
                      self.offerone_4,self.offerone_5,self.offerone_6,self.offerone_7,
                      self.offerone_8,self.offerone_9][self.numberdraw1] == 0:
            self.beliefpayoff1 = 1 + random.choice(Constants.binvec) * 3

        self.numberdraw2 = random.choice(range(0,10))

        if [self.offertwo_0,self.offertwo_1,self.offertwo_2,self.offertwo_3,
                    self.offertwo_4,self.offertwo_5,self.offertwo_6,self.offertwo_7,
                    self.offertwo_8,self.offertwo_9][self.numberdraw2] == 1:
            if self.pickbel2 > 4:
                self.beliefpayoff2 = 4 - self.numberdraw2/10
            elif self.pickbel2 == 4:
                self.beliefpayoff2 = 1 + random.choice(Constants.mediancutvec) * 3 - self.numberdraw2/10
            elif self.pickbel2 < 4:
                self.beliefpayoff2 = 1 - self.numberdraw2/10

        if [self.offertwo_0,self.offertwo_1,self.offertwo_2,self.offertwo_3,
                    self.offertwo_4,self.offertwo_5,self.offertwo_6,self.offertwo_7,
                    self.offertwo_8,self.offertwo_9][self.numberdraw2] == 0:
            self.beliefpayoff2 = 1 + random.choice(Constants.binvec) * 3

        self.payoffbelief = random.choice([self.beliefpayoff1,self.beliefpayoff2])

        self.participant.vars['p11'] = self.payoffdec1
        self.participant.vars['p12'] = self.payoffbelief