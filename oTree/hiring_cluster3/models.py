from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random


author = 'Stefan Gehrig'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'hiring_cluster3'
    players_per_group = None
    tasks = ['A','B','C','D']
    num_rounds = len(tasks)
    incent_binary = (6)
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

    dec6 = models.BooleanField()
    dec7 = models.BooleanField()
    dec8 = models.BooleanField()
    dec9 = models.BooleanField()

    treat = models.CharField()

    indif6 = models.BooleanField()
    indif7 = models.BooleanField()
    indif8 = models.BooleanField()
    indif9 = models.BooleanField()

    payoffdec6 = models.CurrencyField()
    payoffdec7 = models.CurrencyField()
    payoffdec8 = models.CurrencyField()
    payoffdec9 = models.CurrencyField()

    pick1 = models.IntegerField()
    pick2 = models.IntegerField()
    pick3 = models.IntegerField()
    pick4 = models.IntegerField()
    pick5 = models.IntegerField()
    pick6 = models.IntegerField()

    def set_payoffs3(self):

        self.pick1 = random.choice(Constants.male_certgk)
        self.pick2 = random.choice(Constants.female_certgk)
        self.pick3 = random.choice(Constants.male_certhf)
        self.pick4 = random.choice(Constants.female_certhf)
        self.pick5 = random.choice(Constants.male_all)
        self.pick6 = random.choice(Constants.female_all)


        if self.indif6 == 0:
            if self.pick5 > self.pick2 and self.dec6 == 1:
                    self.payoffdec6 = Constants.incent_binary
            elif self.pick5 < self.pick2 and self.dec6 == 0:
                    self.payoffdec6 = Constants.incent_binary
            elif self.pick5 < self.pick2 and self.dec6 == 1:
                    self.payoffdec6 = 0
            elif self.pick5 > self.pick2 and self.dec6 == 0:
                    self.payoffdec6 = 0
            elif self.pick5 == self.pick2:
                    self.payoffdec6 = Constants.incent_binary * random.choice(Constants.binvec)
        else:
            self.payoffdec6 = 0.1 + Constants.incent_binary * random.choice(Constants.binvec)

        if self.indif7 == 0:
            if self.pick5 > self.pick4 and self.dec7 == 1:
                    self.payoffdec7 = Constants.incent_binary
            elif self.pick5 < self.pick4 and self.dec7 == 0:
                    self.payoffdec7 = Constants.incent_binary
            elif self.pick5 < self.pick4 and self.dec7 == 1:
                    self.payoffdec7 = 0
            elif self.pick5 > self.pick4 and self.dec7 == 0:
                    self.payoffdec7 = 0
            elif self.pick5 == self.pick4:
                    self.payoffdec7 = Constants.incent_binary * random.choice(Constants.binvec)
        else:
            self.payoffdec7 = 0.1 + Constants.incent_binary * random.choice(Constants.binvec)

        if self.indif8 == 0:
            if self.pick1 > self.pick6 and self.dec8 == 1:
                    self.payoffdec8 = Constants.incent_binary
            elif self.pick1 < self.pick6 and self.dec8 == 0:
                    self.payoffdec8 = Constants.incent_binary
            elif self.pick1 < self.pick6 and self.dec8 == 1:
                    self.payoffdec8 = 0
            elif self.pick1 > self.pick6 and self.dec8 == 0:
                    self.payoffdec8 = 0
            elif self.pick1 == self.pick6:
                    self.payoffdec8 = Constants.incent_binary * random.choice(Constants.binvec)
        else:
            self.payoffdec8 = 0.1 + Constants.incent_binary * random.choice(Constants.binvec)

        if self.indif9 == 0:
            if self.pick3 > self.pick6 and self.dec9 == 1:
                    self.payoffdec9 = Constants.incent_binary
            elif self.pick3 < self.pick6 and self.dec9 == 0:
                    self.payoffdec9 = Constants.incent_binary
            elif self.pick3 < self.pick6 and self.dec9 == 1:
                    self.payoffdec9 = 0
            elif self.pick3 > self.pick6 and self.dec9 == 0:
                    self.payoffdec9 = 0
            elif self.pick3 == self.pick6:
                    self.payoffdec9 = Constants.incent_binary * random.choice(Constants.binvec)
        else:
            self.payoffdec9 = 0.1 + Constants.incent_binary * random.choice(Constants.binvec)

        self.participant.vars['p6'] = self.payoffdec6
        self.participant.vars['p7'] = self.payoffdec7
        self.participant.vars['p8'] = self.payoffdec8
        self.participant.vars['p9'] = self.payoffdec9