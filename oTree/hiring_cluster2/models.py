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
    name_in_url = 'hiring_cluster2'
    players_per_group = None
    tasks = ['A','B','C','D']
    incent_binary = (6)
    num_rounds = len(tasks)
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


class Subsession(BaseSubsession):
    def creating_session(self):
        for player in self.get_players():
            player.treat = random.choice(['treatA', 'treatB'])
        if self.round_number == 1:
            for p in self.get_players():
                round_numbers = list(range(1, Constants.num_rounds+1))
                random.shuffle(round_numbers)
                p.participant.vars['task_rounds'] = dict(zip(Constants.tasks, round_numbers))


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    dec2 = models.BooleanField()
    dec3 = models.BooleanField()
    dec4 = models.BooleanField()
    dec5 = models.BooleanField()
    treat = models.CharField()

    indif2 = models.BooleanField()
    indif3 = models.BooleanField()
    indif4 = models.BooleanField()
    indif5 = models.BooleanField()

    payoffdec2 = models.CurrencyField()
    payoffdec3 = models.CurrencyField()
    payoffdec4 = models.CurrencyField()
    payoffdec5 = models.CurrencyField()

    pick1 = models.IntegerField()
    pick2 = models.IntegerField()
    pick3 = models.IntegerField()
    pick4 = models.IntegerField()

    def set_payoffs2(self):

        self.pick1 = random.choice(Constants.male_certgk)
        self.pick2 = random.choice(Constants.female_certgk)
        self.pick3 = random.choice(Constants.male_certhf)
        self.pick4 = random.choice(Constants.female_certhf)


        if self.indif2 == 0:
            if self.pick1 > self.pick2 and self.dec2 == 1:
                    self.payoffdec2 = Constants.incent_binary
            elif self.pick1 < self.pick2 and self.dec2 == 0:
                    self.payoffdec2 = Constants.incent_binary
            elif self.pick1 < self.pick2 and self.dec2 == 1:
                    self.payoffdec2 = 0
            elif self.pick1 > self.pick2 and self.dec2 == 0:
                    self.payoffdec2 = 0
            elif self.pick1 == self.pick2:
                    self.payoffdec2 = Constants.incent_binary * random.choice(Constants.binvec)
        else:
            self.payoffdec2 = 0.1 + Constants.incent_binary * random.choice(Constants.binvec)

        if self.indif3 == 0:
            if self.pick3 > self.pick4 and self.dec3 == 1:
                    self.payoffdec3 = Constants.incent_binary
            elif self.pick3 < self.pick4 and self.dec3 == 0:
                    self.payoffdec3 = Constants.incent_binary
            elif self.pick3 < self.pick4 and self.dec3 == 1:
                    self.payoffdec3 = 0
            elif self.pick3 > self.pick4 and self.dec3 == 0:
                    self.payoffdec3 = 0
            elif self.pick3 == self.pick4:
                    self.payoffdec3 = Constants.incent_binary * random.choice(Constants.binvec)
        else:
            self.payoffdec3 = 0.1 + Constants.incent_binary * random.choice(Constants.binvec)

        if self.indif4 == 0:
            if self.pick2 > self.pick4 and self.dec4 == 1:
                    self.payoffdec4 = Constants.incent_binary
            elif self.pick2 < self.pick4 and self.dec4 == 0:
                    self.payoffdec4 = Constants.incent_binary
            elif self.pick2 < self.pick4 and self.dec4 == 1:
                    self.payoffdec4 = 0
            elif self.pick2 > self.pick4 and self.dec4 == 0:
                    self.payoffdec4 = 0
            elif self.pick2 == self.pick4:
                    self.payoffdec4 = Constants.incent_binary * random.choice(Constants.binvec)
        else:
            self.payoffdec4 = 0.1 + Constants.incent_binary * random.choice(Constants.binvec)

        if self.indif5 == 0:
            if self.pick1 > self.pick3 and self.dec5 == 1:
                    self.payoffdec5 = Constants.incent_binary
            elif self.pick1 < self.pick3 and self.dec5 == 0:
                    self.payoffdec5 = Constants.incent_binary
            elif self.pick1 < self.pick3 and self.dec5 == 1:
                    self.payoffdec5 = 0
            elif self.pick1 > self.pick3 and self.dec5 == 0:
                    self.payoffdec5 = 0
            elif self.pick1 == self.pick3:
                    self.payoffdec5 = Constants.incent_binary * random.choice(Constants.binvec)
        else:
            self.payoffdec5 = 0.1 + Constants.incent_binary * random.choice(Constants.binvec)

        self.participant.vars['p2'] = self.payoffdec2
        self.participant.vars['p3'] = self.payoffdec3
        self.participant.vars['p4'] = self.payoffdec4
        self.participant.vars['p5'] = self.payoffdec5




