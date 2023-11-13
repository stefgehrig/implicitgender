from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random

author = 'Stefan Gehrig'

doc = """
Your app description
"""

from django.core.validators import (MaxValueValidator, MinValueValidator)


class Subsession(BaseSubsession):

    def creating_session(self):
        if self.round_number == 1:
            self.group_randomly()
        else:
            self.group_like_round(1)

    p_male_better1 = models.IntegerField()
    p_male_better2 = models.IntegerField()
    p_male_better3 = models.IntegerField()
    p_male_better4 = models.IntegerField()
    p_male_better5 = models.IntegerField()
    p_male_better6 = models.IntegerField()
    p_male_better7 = models.IntegerField()

    def set_gendercomparisons(self):

        all_players = self.get_players()

        all_male = [p for p in all_players if p.gen == 2]
        all_female = [p for p in all_players if p.gen == 1]

        pairs = []
        for p_m in all_male:
            for p_f in all_female:
                pairs.append((p_m, p_f))

        assert len(pairs) == len(all_male) * len(all_female)

        n_male_better1 = 0

        for pair in pairs:
            p_m, p_f = pair
            if p_m.resultKnowS > p_f.resultKnowS:
                n_male_better1 += 1
            elif p_m.resultKnowS == p_f.resultKnowS:
                chance = (random.randint(1, 100))
                if chance <= 50:
                    n_male_better1 += 1
                elif chance > 50:
                    n_male_better1 += 0

        self.p_male_better1 = int(round(n_male_better1 / len(pairs) * 100))

        n_male_better2 = 0

        for pair in pairs:
            p_m, p_f = pair
            if p_m.resultSumming > p_f.resultSumming:
                n_male_better2 += 1
            elif p_m.resultSumming == p_f.resultSumming:
                chance = (random.randint(1, 100))
                if chance <= 50:
                    n_male_better2 += 1
                elif chance > 50:
                    n_male_better2 += 0

        self.p_male_better2 = int(round(n_male_better2 / len(pairs) * 100))

        n_male_better3 = 0

        for pair in pairs:
            p_m, p_f = pair
            if p_m.resultWordsall > p_f.resultWordsall:
                n_male_better1 += 1
            elif p_m.resultWordsall == p_f.resultWordsall:
                chance = (random.randint(1, 100))
                if chance <= 50:
                    n_male_better3 += 1
                elif chance > 50:
                    n_male_better3 += 0

        self.p_male_better3 = int(round(n_male_better3 / len(pairs) * 100))

        n_male_better4 = 0

        for pair in pairs:
            p_m, p_f = pair
            if p_m.resultMat > p_f.resultMat:
                n_male_better1 += 1
            elif p_m.resultMat == p_f.resultMat:
                chance = (random.randint(1, 100))
                if chance <= 50:
                    n_male_better4 += 1
                elif chance > 50:
                    n_male_better4 += 0

        self.p_male_better4 = int(round(n_male_better4 / len(pairs) * 100))

        n_male_better5 = 0

        for pair in pairs:
            p_m, p_f = pair
            if p_m.resultFig > p_f.resultFig:
                n_male_better1 += 1
            elif p_m.resultFig == p_f.resultFig:
                chance = (random.randint(1, 100))
                if chance <= 50:
                    n_male_better5 += 1
                elif chance > 50:
                    n_male_better5 += 0

        self.p_male_better5 = int(round(n_male_better5 / len(pairs) * 100))

        n_male_better6 = 0

        for pair in pairs:
            p_m, p_f = pair
            if p_m.resultEQ > p_f.resultEQ:
                n_male_better6 += 1
            elif p_m.resultEQ == p_f.resultEQ:
                chance = (random.randint(1, 100))
                if chance <= 50:
                    n_male_better6 += 1
                elif chance > 50:
                    n_male_better6 += 0

        self.p_male_better6 = int(round(n_male_better6 / len(pairs) * 100))

        n_male_better7 = 0

        for pair in pairs:
            p_m, p_f = pair
            if p_m.resultKnowGplayer > p_f.resultKnowGplayer:
                n_male_better7 += 1
            elif p_m.resultKnowGplayer == p_f.resultKnowGplayer:
                chance = (random.randint(1, 100))
                if chance <= 50:
                    n_male_better7 += 1
                elif chance > 50:
                    n_male_better7 += 0

        self.p_male_better7 = int(round(n_male_better7 / len(pairs) * 100))


class Constants(BaseConstants):
    name_in_url = 'stimuli'
    players_per_group = 2
    num_rounds = 1
    pointsSumming = c(0.5)
    timeSumming = 4 * 60
    pointsKnowG = c(0.3)
    timeKnowG = 4 * 60
    pointsKnowS = c(0.6)
    timeKnowS = 4 * 60
    timeMat = 5 * 60
    pointsMat = c(1.3)
    pointsWord = c(0.4)
    timeWord1 = 90
    timeWord2 = 90
    timeWord3 = 90
    pointsFig = c(0.9)
    timeFig = 100
    KnowSR1 = 2
    KnowSR2 = 2
    KnowSR3 = 1
    KnowSR4 = 2
    KnowSR5 = 4
    KnowSR6 = 1
    KnowSR7 = 4
    KnowSR8 = 3
    KnowSR9 = 1
    KnowSR10 = 1
    KnowSR11 = 3
    KnowSR12 = 3
    KnowSR13 = 4
    KnowSR14 = 1
    KnowSR15 = 2
    KnowSR16 = 4
    KnowSR17 = 4
    KnowSR18 = 1
    KnowSR19 = 3
    KnowSR20 = 4
    KnowSR21 = 2
    KnowSR22 = 2
    KnowSR23 = 1
    KnowSR24 = 3
    KnowSR25 = 1
    KnowSR26 = 3
    KnowSR27 = 4
    KnowSR28 = 1
    KnowSR29 = 3
    KnowSR30 = 3
    SummingR1 = 167
    SummingR2 = 326
    SummingR3 = 208
    SummingR4 = 180
    SummingR5 = 208
    SummingR6 = 256
    SummingR7 = 241
    SummingR8 = 173
    SummingR9 = 180
    SummingR10 = 262
    SummingR11 = 297
    SummingR12 = 99
    SummingR13 = 257
    SummingR14 = 195
    SummingR15 = 170
    SummingR16 = 287
    SummingR17 = 243
    SummingR18 = 282
    SummingR19 = 161
    SummingR20 = 241
    SummingR21 = 163
    SummingR22 = 196
    SummingR23 = 269
    SummingR24 = 208
    SummingR25 = 213
    SummingR26 = 261
    SummingR27 = 298
    SummingR28 = 169
    SummingR29 = 290
    SummingR30 = 207
    KnowGR1 = 2
    KnowGR2 = 2
    KnowGR3 = 1
    KnowGR4 = 2
    KnowGR5 = 4
    KnowGR6 = 1
    KnowGR7 = 4
    KnowGR8 = 3
    KnowGR9 = 1
    KnowGR10 = 1
    KnowGR11 = 3
    KnowGR12 = 3
    KnowGR13 = 4
    KnowGR14 = 1
    KnowGR15 = 2
    KnowGR16 = 4
    KnowGR17 = 4
    KnowGR18 = 1
    KnowGR19 = 3
    KnowGR20 = 4
    KnowGR21 = 2
    KnowGR22 = 2
    KnowGR23 = 1
    KnowGR24 = 3
    KnowGR25 = 1
    KnowGR26 = 3
    KnowGR27 = 4
    KnowGR28 = 1
    KnowGR29 = 3
    KnowGR30 = 3
    Mat1R = 4
    Mat2R = 5
    Mat3R = 2
    Mat4R = 2
    Mat5R = 3
    Mat6R = 5
    Mat7R = 4
    Mat8R = 1
    Mat9R = 4
    Mat10R = 5
    Fig1R = 1
    Fig2R = 3
    Fig3R = 1
    Fig4R = 2
    Fig5R = 1
    Fig6R = 3
    Fig7R = 2
    Fig8R = 3
    Fig9R = 3
    Fig10R = 2
    tasklist = ['Allgemeine Wissensfragen', 'Mathematik', 'Worträtsel', 'Muster Erkennen', 'Versteckte Formen']


class Group(BaseGroup):

    resultKnowG = models.IntegerField()

    def set_feedb_KnowGresult(self):
        p1 = self.get_player_by_id(1)
        p2 = self.get_player_by_id(2)

        self.resultKnowG = 0

        for x in range(1, 25):
            p1KnowG = getattr(p1, 'KnowG%d' % x)
            p2KnowG = getattr(p2, 'KnowG%d' % x)
            rKnowG = getattr(Constants, 'KnowGR%d' % x)
            if p1KnowG == p2KnowG == rKnowG:
                self.resultKnowG += 1
            else:
                self.resultKnowG += 0


class Player(BasePlayer):
    KnowS1 = models.IntegerField(
        choices=[
            [1, 'Sauerstoff'],
            [2, 'Stickstoff'],
            [3, 'Helium'],
            [4, 'Wasserdampf'], ],
        widget=widgets.RadioSelect()
    )
    KnowS2 = models.IntegerField(
        choices=[
            [1, 'Kolumbien'],
            [2, 'England'],
            [3, 'Brasilien'],
            [4, 'Ghana'], ],
        widget=widgets.RadioSelect()
    )
    KnowS3 = models.IntegerField(choices=[
        [1, 'Scrubs'],
        [2, 'How I Met Your Mother'],
        [3, 'Hausmeister Krause'],
        [4, 'Big Bang Theory'], ],
        widget=widgets.RadioSelect())
    KnowS4 = models.IntegerField(
        choices=[
            [1, 'Kaiser Wilhelm II.'],
            [2, 'Fürst von Metternich'],
            [3, 'Friedrich der Große'],
            [4, 'Friedrich Ebert'], ],
        widget=widgets.RadioSelect()
    )
    KnowS5 = models.IntegerField(
        choices=[
            [1, 'Zellkern, Zellwand, Zellmembran'],
            [2, 'Zellkern, Zytoplasma, Vakuole'],
            [3, 'Mitochondrien, Zellmembran, Plastiden'],
            [4, 'Zellkern, Zytoplasma, Zellmembran'], ],
        widget=widgets.RadioSelect()
    )
    KnowS6 = models.IntegerField(
        choices=[
            [1, 'Kongo'],
            [2, 'Mali'],
            [3, 'Sudan'],
            [4, 'Somalia'], ],
        widget=widgets.RadioSelect()
    )
    KnowS7 = models.IntegerField(
        choices=[
            [1, 'Madonna'],
            [2, 'Dido'],
            [3, 'Rihanna'],
            [4, 'Pink'], ],
        widget=widgets.RadioSelect()
    )
    KnowS8 = models.IntegerField(
        choices=[
            [1, 'Überdosis'],
            [2, 'Krebs'],
            [3, 'Flugzeugabsturz'],
            [4, 'Autounfall'], ],
        widget=widgets.RadioSelect()
    )
    KnowS9 = models.IntegerField(
        choices=[
            [1, 'Roman'],
            [2, 'Gedicht'],
            [3, 'Drama'],
            [4, 'Märchen'], ],
        widget=widgets.RadioSelect()
    )
    KnowS10 = models.IntegerField(
        choices=[
            [1, 'Babylon'],
            [2, 'Rhodos'],
            [3, 'Ephesus'],
            [4, 'Alexandria'], ],
        widget=widgets.RadioSelect()
    )
    KnowS11 = models.IntegerField(
        choices=[
            [1, 'Rom'],
            [2, 'New York'],
            [3, 'Peking'],
            [4, 'Istanbul'], ],
        widget=widgets.RadioSelect()
    )
    KnowS12 = models.IntegerField(
        choices=[
            [1, 'Ausrufung der ersten deutschen Republik'],
            [2, 'Verfolgung von Juden in der Reichspogromnacht '],
            [3, 'Ernennung Hitlers zum Reichskanzler'],
            [4, 'Fall der Berliner Mauer'], ],
        widget=widgets.RadioSelect()
    )
    KnowS13 = models.IntegerField(
        choices=[
            [1, 'Der 30-jährige Krieg endete'],
            [2, 'Die Französische Revolution begann'],
            [3, 'Napoleon krönte sich zum Kaiser'],
            [4, 'Die USA erklären ihre Unabhängigkeit'], ],
        widget=widgets.RadioSelect()
    )
    KnowS19 = models.IntegerField(
        choices=[
            [1, 'Van Gogh'],
            [2, 'Picasso'],
            [3, 'Michelangelo'],
            [4, 'Rembrandt'], ],
        widget=widgets.RadioSelect()
    )
    KnowS15 = models.IntegerField(
        choices=[
            [1, 'Ernest Hemingway'],
            [2, 'Oscar Wilde'],
            [3, 'Marc Twain'],
            [4, 'John Steinbeck'], ],
        widget=widgets.RadioSelect()
    )
    KnowS16 = models.IntegerField(
        choices=[
            [1, 'Themen der antiken Mythologie'],
            [2, 'Wirklichkeitsgetreue, sachliche Form'],
            [3, 'Religiöse Motive'],
            [4, 'Spielerische und dekorative Elemente'], ],
        widget=widgets.RadioSelect()
    )
    KnowS17 = models.IntegerField(
        choices=[
            [1, 'Alkohol'],
            [2, 'Zucker'],
            [3, 'Glycerin'],
            [4, 'Kochsalz'], ],
        widget=widgets.RadioSelect()
    )
    KnowS18 = models.IntegerField(
        choices=[
            [1, '„Heute ist Mama gestorben. Vielleicht auch gestern, ich weiß es nicht.“'],
            [2, '„Am Anfang war eine Landschaft.“'],
            [3, '„Falls Sie wirklich meine Geschichte hören wollen…“'],
            [4,
             '„Im achtzehnten Jahrhundert lebte in Frankreich ein Mann, der zu den genialsten und abscheulichsten Gestalten dieser an genialen und abscheulichen Gestalten nicht armen Epoche gehörte.“'], ],
        widget=widgets.RadioSelect()
    )
    KnowS14 = models.IntegerField(
        choices=[
            [1, 'Keine der drei'],
            [2, 'Simbabwe und Kongo'],
            [3, 'Argentinien und Peru'],
            [4, 'Bulgarien und Moldawien'], ],
        widget=widgets.RadioSelect()
    )
    KnowS21 = models.IntegerField(
        choices=[
            [1, 'Pablo Picasso'],
            [2, 'Franz Marc'],
            [3, 'Claude Monet'],
            [4, 'Gustav Klimt'], ],
        widget=widgets.RadioSelect()
    )
    KnowS20 = models.IntegerField(
        choices=[
            [1, 'ca. 19 km'],
            [2, 'ca. 15 km'],
            [3, 'ca. 21 km'],
            [4, 'ca. 11 km'], ],
        widget=widgets.RadioSelect()
    )
    KnowS22 = models.IntegerField(
        choices=[
            [1, 'Berlin Alexanderplatz'],
            [2, 'Dantons Tod'],
            [3, 'Michael Kohlhaas'],
            [4, 'Der zerbrochene Krug'], ],
        widget=widgets.RadioSelect()
    )
    KnowS23 = models.IntegerField(
        choices=[
            [1, 'Schwefeldioxid'],
            [2, 'Chlor'],
            [3, 'Fluor'],
            [4, 'Kohlenmonoxid'], ],
        widget=widgets.RadioSelect()
    )
    KnowS24 = models.IntegerField(
        choices=[
            [1, 'Zugspitze'],
            [2, 'Matterhorn'],
            [3, 'Großglockner'],
            [4, 'Wildspitze'], ],
        widget=widgets.RadioSelect()
    )

    KnowS25 = models.IntegerField(
        choices=[
            [1, 'Les femmes d’Alger (Picasso)'],
            [2, 'Three Studies of Lucian Freud (Bacon)'],
            [3, 'Der Schrei (Munch)'],
            [4, 'Sonnenblumen (van Gogh)'], ],
        widget=widgets.RadioSelect()
    )

    KnowS26 = models.IntegerField(
        choices=[
            [1, 'George Clooney'],
            [2, 'Jack Nicholson'],
            [3, 'Leonardo DiCaprio'],
            [4, 'Matthew McConaughey'], ],
        widget=widgets.RadioSelect()
    )

    KnowS27 = models.IntegerField(
        choices=[
            [1, 'New York'],
            [2, 'Paris'],
            [3, 'Prag'],
            [4, 'London'], ],
        widget=widgets.RadioSelect()
    )

    KnowS28 = models.IntegerField(
        choices=[
            [1, 'Kiefer'],
            [2, 'Seerose'],
            [3, 'Bambus'],
            [4, 'Reis'], ],
        widget=widgets.RadioSelect()
    )

    KnowS29 = models.IntegerField(
        choices=[
            [1, 'Max Liebermann'],
            [2, 'Paul Cézanne'],
            [3, 'Wassily Kandinsky'],
            [4, 'Édouard Manet'], ],
        widget=widgets.RadioSelect()
    )

    KnowS30 = models.IntegerField(
        choices=[
            [1, 'Vanessa'],
            [2, 'Sandy'],
            [3, 'Indira'],
            [4, 'Jessica'], ],
        widget=widgets.RadioSelect()
    )

    resultKnowS = models.IntegerField()

    def set_feedb_KnowS(self):

        self.resultKnowS = 0

        for x in range(1, 31):
            pKnowS = getattr(self, 'KnowS%d' % x)
            rKnowS = getattr(Constants, 'KnowSR%d' % x)
            if pKnowS == rKnowS:
                self.resultKnowS += 1
            else:
                self.resultKnowS += 0

    resultSumming = models.IntegerField()
    Summing1 = models.IntegerField()
    Summing2 = models.IntegerField()
    Summing3 = models.IntegerField()
    Summing4 = models.IntegerField()
    Summing5 = models.IntegerField()
    Summing6 = models.IntegerField()
    Summing7 = models.IntegerField()
    Summing8 = models.IntegerField()
    Summing9 = models.IntegerField()
    Summing10 = models.IntegerField()
    Summing11 = models.IntegerField()
    Summing12 = models.IntegerField()
    Summing13 = models.IntegerField()
    Summing14 = models.IntegerField()
    Summing15 = models.IntegerField()
    Summing16 = models.IntegerField()
    Summing17 = models.IntegerField()
    Summing18 = models.IntegerField()
    Summing19 = models.IntegerField()
    Summing20 = models.IntegerField()
    Summing21 = models.IntegerField()
    Summing22 = models.IntegerField()
    Summing23 = models.IntegerField()
    Summing24 = models.IntegerField()
    Summing25 = models.IntegerField()
    Summing26 = models.IntegerField()
    Summing27 = models.IntegerField()
    Summing28 = models.IntegerField()
    Summing29 = models.IntegerField()
    Summing30 = models.IntegerField()

    def set_feedb_Summing(self):

        self.resultSumming = 0

        for x in range(1, 31):
            pSumming = getattr(self, 'Summing%d' % x)
            rSumming = getattr(Constants, 'SummingR%d' % x)
            if pSumming == rSumming:
                self.resultSumming += 1
            else:
                self.resultSumming += 0

    word1 = models.BooleanField(
        widget=widgets.CheckboxInput()
    )
    word2 = models.BooleanField(
        widget=widgets.CheckboxInput()
    )
    word3 = models.BooleanField(
        widget=widgets.CheckboxInput()
    )
    word4 = models.BooleanField(
        widget=widgets.CheckboxInput()
    )
    word5 = models.BooleanField(
        widget=widgets.CheckboxInput()
    )
    word6 = models.BooleanField(
        widget=widgets.CheckboxInput()
    )
    word7 = models.BooleanField(
        widget=widgets.CheckboxInput()
    )
    word8 = models.BooleanField(
        widget=widgets.CheckboxInput()
    )
    word9 = models.BooleanField(
        widget=widgets.CheckboxInput()
    )
    word10 = models.BooleanField(
        widget=widgets.CheckboxInput()
    )
    word11 = models.BooleanField(
        widget=widgets.CheckboxInput()
    )
    word12 = models.BooleanField(
        widget=widgets.CheckboxInput()
    )
    word13 = models.BooleanField(
        widget=widgets.CheckboxInput()
    )
    word14 = models.BooleanField(
        widget=widgets.CheckboxInput()
    )
    word15 = models.BooleanField(
        widget=widgets.CheckboxInput()
    )
    word16 = models.BooleanField(
        widget=widgets.CheckboxInput()
    )
    word17 = models.BooleanField(
        widget=widgets.CheckboxInput()
    )
    word18 = models.BooleanField(
        widget=widgets.CheckboxInput()
    )
    word19 = models.BooleanField(
        widget=widgets.CheckboxInput()
    )
    word20 = models.BooleanField(
        widget=widgets.CheckboxInput()
    )
    word21 = models.BooleanField(
        widget=widgets.CheckboxInput()
    )
    word22 = models.BooleanField(
        widget=widgets.CheckboxInput()
    )
    word23 = models.BooleanField(
        widget=widgets.CheckboxInput()
    )
    word24 = models.BooleanField(
        widget=widgets.CheckboxInput()
    )
    word25 = models.BooleanField(
        widget=widgets.CheckboxInput()
    )
    word26 = models.BooleanField(
        widget=widgets.CheckboxInput()
    )
    word27 = models.BooleanField(
        widget=widgets.CheckboxInput()
    )
    word28 = models.BooleanField(
        widget=widgets.CheckboxInput()
    )
    word29 = models.BooleanField(
        widget=widgets.CheckboxInput()
    )
    word30 = models.BooleanField(
        widget=widgets.CheckboxInput()
    )

    counter_total_1 = models.IntegerField()
    counter_correct_1 = models.IntegerField()
    counter_total_2 = models.IntegerField()
    counter_correct_2 = models.IntegerField()
    counter_total_3 = models.IntegerField()
    counter_correct_3 = models.IntegerField()


    def count_1(self):

        self.counter_total_1 = 0
        for i in range(1, 31):
            word = getattr(self, 'word%d' % i)
            if word == 1:
                self.counter_total_1 += 1

        self.counter_correct_1 = 0
        if self.word1 == 1:
            self.counter_correct_1 += 1
        if self.word2 == 1:
            self.counter_correct_1 += 1
        if self.word3 == 1:
            self.counter_correct_1 += 1
        if self.word7 == 1:
            self.counter_correct_1 += 1
        if self.word9 == 1:
            self.counter_correct_1 += 1
        if self.word11 == 1:
            self.counter_correct_1 += 1
        if self.word17 == 1:
            self.counter_correct_1 += 1
        if self.word25 == 1:
            self.counter_correct_1 += 1
        if self.word27 == 1:
            self.counter_correct_1 += 1
        if self.word28 == 1:
            self.counter_correct_1 += 1


    def count_2(self):
        self.counter_total_2 = 0
        for i in range(1, 31):
            word = getattr(self, 'word%d' % i)
            if word == 1:
                self.counter_total_2 += 1
        self.counter_correct_2 = 0
        if self.word2 == 1:
            self.counter_correct_2 += 1
        if self.word7 == 1:
            self.counter_correct_2 += 1
        if self.word9 == 1:
            self.counter_correct_2 += 1
        if self.word11 == 1:
            self.counter_correct_2 += 1
        if self.word12 == 1:
            self.counter_correct_2 += 1
        if self.word17 == 1:
            self.counter_correct_2 += 1
        if self.word18 == 1:
            self.counter_correct_2 += 1
        if self.word22 == 1:
            self.counter_correct_2 += 1
        if self.word24 == 1:
            self.counter_correct_2 += 1
        if self.word25 == 1:
            self.counter_correct_2 += 1


    def count_3(self):
        self.counter_total_3 = 0
        for i in range(1, 31):
            word = getattr(self, 'word%d' % i)
            if word == 1:
                self.counter_total_3 += 1
        self.counter_correct_3 = 0
        if self.word4 == 1:
            self.counter_correct_3 += 1
        if self.word5 == 1:
            self.counter_correct_3 += 1
        if self.word9 == 1:
            self.counter_correct_3 += 1
        if self.word11 == 1:
            self.counter_correct_3 += 1
        if self.word12 == 1:
            self.counter_correct_3 += 1
        if self.word16 == 1:
            self.counter_correct_3 += 1
        if self.word21 == 1:
            self.counter_correct_3 += 1
        if self.word22 == 1:
            self.counter_correct_3 += 1
        if self.word24 == 1:
            self.counter_correct_3 += 1
        if self.word26 == 1:
            self.counter_correct_3 += 1


    counterWordsall = models.IntegerField()
    resultWordsall = models.IntegerField()
    failuresWordsall = models.IntegerField()

    def count_all(self):
        self.failuresWordsall = (self.counter_total_3 - self.counter_correct_3) + (self.counter_total_2 - self.counter_correct_2) + (self.counter_total_1 - self.counter_correct_1)
        self.counterWordsall = self.counter_correct_1 + self.counter_correct_2 + self.counter_correct_3
        if self.counterWordsall < self.failuresWordsall:
            self.resultWordsall = 0
        else:
            self.resultWordsall = self.counterWordsall - self.failuresWordsall

    Mat1 = models.IntegerField(
        choices=[
            [1, 'A'],
            [2, 'B'],
            [3, 'C'],
            [4, 'D'],
            [5, 'E'],
            [6, 'F'], ],
        widget=widgets.RadioSelectHorizontal()
    )
    Mat2 = models.IntegerField(
        choices=[
            [1, 'A'],
            [2, 'B'],
            [3, 'C'],
            [4, 'D'],
            [5, 'E'],
            [6, 'F'], ],
        widget=widgets.RadioSelectHorizontal()
    )
    Mat3 = models.IntegerField(
        choices=[
            [1, 'A'],
            [2, 'B'],
            [3, 'C'],
            [4, 'D'],
            [5, 'E'],
            [6, 'F'], ],
        widget=widgets.RadioSelectHorizontal()
    )
    Mat4 = models.IntegerField(
        choices=[
            [1, 'A'],
            [2, 'B'],
            [3, 'C'],
            [4, 'D'],
            [5, 'E'],
            [6, 'F'], ],
        widget=widgets.RadioSelectHorizontal()
    )
    Mat5 = models.IntegerField(
        choices=[
            [1, 'A'],
            [2, 'B'],
            [3, 'C'],
            [4, 'D'],
            [5, 'E'],
            [6, 'F'], ],
        widget=widgets.RadioSelectHorizontal()
    )
    Mat6 = models.IntegerField(
        choices=[
            [1, 'A'],
            [2, 'B'],
            [3, 'C'],
            [4, 'D'],
            [5, 'E'],
            [6, 'F'], ],
        widget=widgets.RadioSelectHorizontal()
    )
    Mat7 = models.IntegerField(
        choices=[
            [1, 'A'],
            [2, 'B'],
            [3, 'C'],
            [4, 'D'],
            [5, 'E'],
            [6, 'F'], ],
        widget=widgets.RadioSelectHorizontal()
    )
    Mat8 = models.IntegerField(
        choices=[
            [1, 'A'],
            [2, 'B'],
            [3, 'C'],
            [4, 'D'],
            [5, 'E'],
            [6, 'F'], ],
        widget=widgets.RadioSelectHorizontal()
    )
    Mat9 = models.IntegerField(
        choices=[
            [1, 'A'],
            [2, 'B'],
            [3, 'C'],
            [4, 'D'],
            [5, 'E'],
            [6, 'F'], ],
        widget=widgets.RadioSelectHorizontal()
    )
    Mat10 = models.IntegerField(
        choices=[
            [1, 'A'],
            [2, 'B'],
            [3, 'C'],
            [4, 'D'],
            [5, 'E'],
            [6, 'F'], ],
        widget=widgets.RadioSelectHorizontal()
    )
    resultMat = models.IntegerField()

    def set_feedb_Mat(self):

        self.resultMat = 0

        for x in range(1, 11):
            pMat = getattr(self, 'Mat%d' % x)
            rMat = getattr(Constants, 'Mat%dR' % x)
            if pMat == rMat:
                self.resultMat += 1
            else:
                self.resultMat += 0

    Fig1 = models.IntegerField(
        choices=[
            [1, 'A'],
            [2, 'B'],
            [3, 'C'], ],
        widget=widgets.RadioSelectHorizontal()
    )
    Fig2 = models.IntegerField(
        choices=[
            [1, 'A'],
            [2, 'B'],
            [3, 'C'], ],
        widget=widgets.RadioSelectHorizontal()
    )
    Fig3 = models.IntegerField(
        choices=[
            [1, 'A'],
            [2, 'B'],
            [3, 'C'], ],
        widget=widgets.RadioSelectHorizontal()
    )
    Fig4 = models.IntegerField(
        choices=[
            [1, 'A'],
            [2, 'B'],
            [3, 'C'], ],
        widget=widgets.RadioSelectHorizontal()
    )
    Fig5 = models.IntegerField(
        choices=[
            [1, 'A'],
            [2, 'B'],
            [3, 'C'], ],
        widget=widgets.RadioSelectHorizontal()
    )
    Fig6 = models.IntegerField(
        choices=[
            [1, 'A'],
            [2, 'B'],
            [3, 'C'], ],
        widget=widgets.RadioSelectHorizontal()
    )
    Fig7 = models.IntegerField(
        choices=[
            [1, 'A'],
            [2, 'B'],
            [3, 'C'], ],
        widget=widgets.RadioSelectHorizontal()
    )
    Fig8 = models.IntegerField(
        choices=[
            [1, 'A'],
            [2, 'B'],
            [3, 'C'], ],
        widget=widgets.RadioSelectHorizontal()
    )
    Fig9 = models.IntegerField(
        choices=[
            [1, 'A'],
            [2, 'B'],
            [3, 'C'], ],
        widget=widgets.RadioSelectHorizontal()
    )
    Fig10 = models.IntegerField(
        choices=[
            [1, 'A'],
            [2, 'B'],
            [3, 'C'], ],
        widget=widgets.RadioSelectHorizontal()
    )

    resultFig = models.IntegerField()

    def set_feedb_Fig(self):

        self.resultFig = 0

        for x in range(1, 11):
            pFig = getattr(self, 'Fig%d' % x)
            rFig = getattr(Constants, 'Fig%dR' % x)
            if pFig == rFig:
                self.resultFig += 1
            else:
                self.resultFig += 0

    nicky = models.CharField(max_length=255)

    def chat_nickname(self):
        self.nicky = 'Spieler {}'.format(self.id_in_group)

    KnowG1 = models.IntegerField(
        choices=[
            [1, 'Sauerstoff'],
            [2, 'Stickstoff'],
            [3, 'Helium'],
            [4, 'Wasserdampf'], ],
        widget=widgets.RadioSelect()
    )
    KnowG2 = models.IntegerField(
        choices=[
            [1, 'Kolumbien'],
            [2, 'England'],
            [3, 'Brasilien'],
            [4, 'Ghana'], ],
        widget=widgets.RadioSelect()
    )
    KnowG3 = models.IntegerField(
        choices=[
            [1, 'Scrubs'],
            [2, 'How I Met Your Mother'],
            [3, 'Hausmeister Krause'],
            [4, 'Big Bang Theory'], ],
        widget=widgets.RadioSelect())
    KnowG4 = models.IntegerField(
        choices=[
            [1, 'Kaiser Wilhelm II.'],
            [2, 'Fürst von Metternich'],
            [3, 'Friedrich der Große'],
            [4, 'Friedrich Ebert'], ],
        widget=widgets.RadioSelect()
    )
    KnowG5 = models.IntegerField(
        choices=[
            [1, 'Zellkern, Zellwand, Zellmembran'],
            [2, 'Zellkern, Zytoplasma, Vakuole'],
            [3, 'Mitochondrien, Zellmembran, Plastiden'],
            [4, 'Zellkern, Zytoplasma, Zellmembran'], ],
        widget=widgets.RadioSelect()
    )
    KnowG6 = models.IntegerField(
        choices=[
            [1, 'Kongo'],
            [2, 'Mali'],
            [3, 'Sudan'],
            [4, 'Somalia'], ],
        widget=widgets.RadioSelect()
    )
    KnowG7 = models.IntegerField(
        choices=[
            [1, 'Madonna'],
            [2, 'Dido'],
            [3, 'Rihanna'],
            [4, 'Pink'], ],
        widget=widgets.RadioSelect()
    )
    KnowG8 = models.IntegerField(
        choices=[
            [1, 'Überdosis'],
            [2, 'Krebs'],
            [3, 'Flugzeugabsturz'],
            [4, 'Autounfall'], ],
        widget=widgets.RadioSelect()
    )
    KnowG9 = models.IntegerField(
        choices=[
            [1, 'Roman'],
            [2, 'Gedicht'],
            [3, 'Drama'],
            [4, 'Märchen'], ],
        widget=widgets.RadioSelect()
    )
    KnowG10 = models.IntegerField(
        choices=[
            [1, 'Babylon'],
            [2, 'Rhodos'],
            [3, 'Ephesus'],
            [4, 'Alexandria'], ],
        widget=widgets.RadioSelect()
    )
    KnowG11 = models.IntegerField(
        choices=[
            [1, 'Rom'],
            [2, 'New York'],
            [3, 'Peking'],
            [4, 'Istanbul'], ],
        widget=widgets.RadioSelect()
    )
    KnowG12 = models.IntegerField(
        choices=[
            [1, 'Ausrufung der ersten deutschen Republik'],
            [2, 'Verfolgung von Juden in der Reichspogromnacht '],
            [3, 'Ernennung Hitlers zum Reichskanzler'],
            [4, 'Fall der Berliner Mauer'], ],
        widget=widgets.RadioSelect()
    )
    KnowG13 = models.IntegerField(
        choices=[
            [1, 'Der 30-jährige Krieg endete'],
            [2, 'Die Französische Revolution begann'],
            [3, 'Napoleon krönte sich zum Kaiser'],
            [4, 'Die USA erklären ihre Unabhängigkeit'], ],
        widget=widgets.RadioSelect()
    )
    KnowG19 = models.IntegerField(
        choices=[
            [1, 'Van Gogh'],
            [2, 'Picasso'],
            [3, 'Michelangelo'],
            [4, 'Rembrandt'], ],
        widget=widgets.RadioSelect()
    )
    KnowG15 = models.IntegerField(
        choices=[
            [1, 'Ernest Hemingway'],
            [2, 'Oscar Wilde'],
            [3, 'Marc Twain'],
            [4, 'John Steinbeck'], ],
        widget=widgets.RadioSelect()
    )
    KnowG16 = models.IntegerField(
        choices=[
            [1, 'Themen der antiken Mythologie'],
            [2, 'Wirklichkeitsgetreue, sachliche Form'],
            [3, 'Religiöse Motive'],
            [4, 'Spielerische und dekorative Elemente'], ],
        widget=widgets.RadioSelect()
    )
    KnowG17 = models.IntegerField(
        choices=[
            [1, 'Alkohol'],
            [2, 'Zucker'],
            [3, 'Glycerin'],
            [4, 'Kochsalz'], ],
        widget=widgets.RadioSelect()
    )
    KnowG18 = models.IntegerField(
        choices=[
            [1, '„Heute ist Mama gestorben. Vielleicht auch gestern, ich weiß es nicht.“'],
            [2, '„Am Anfang war eine Landschaft.“'],
            [3, '„Falls Sie wirklich meine Geschichte hören wollen…“'],
            [4,
             '„Im achtzehnten Jahrhundert lebte in Frankreich ein Mann, der zu den genialsten und abscheulichsten Gestalten dieser an genialen und abscheulichen Gestalten nicht armen Epoche gehörte.“'], ],
        widget=widgets.RadioSelect()
    )
    KnowG14 = models.IntegerField(
        choices=[
            [1, 'Keine der drei'],
            [2, 'Simbabwe und Kongo'],
            [3, 'Argentinien und Peru'],
            [4, 'Bulgarien und Moldawien'], ],
        widget=widgets.RadioSelect()
    )
    KnowG21 = models.IntegerField(
        choices=[
            [1, 'Pablo Picasso'],
            [2, 'Franz Marc'],
            [3, 'Claude Monet'],
            [4, 'Gustav Klimt'], ],
        widget=widgets.RadioSelect()
    )
    KnowG20 = models.IntegerField(
        choices=[
            [1, 'ca. 19 km'],
            [2, 'ca. 15 km'],
            [3, 'ca. 21 km'],
            [4, 'ca. 11 km'], ],
        widget=widgets.RadioSelect()
    )
    KnowG22 = models.IntegerField(
        choices=[
            [1, 'Berlin Alexanderplatz'],
            [2, 'Dantons Tod'],
            [3, 'Michael Kohlhaas'],
            [4, 'Der zerbrochene Krug'], ],
        widget=widgets.RadioSelect()
    )
    KnowG23 = models.IntegerField(
        choices=[
            [1, 'Schwefeldioxid'],
            [2, 'Chlor'],
            [3, 'Fluor'],
            [4, 'Kohlenmonoxid'], ],
        widget=widgets.RadioSelect()
    )
    KnowG24 = models.IntegerField(
        choices=[
            [1, 'Zugspitze'],
            [2, 'Matterhorn'],
            [3, 'Großglockner'],
            [4, 'Wildspitze'], ],
        widget=widgets.RadioSelect()
    )

    KnowG25 = models.IntegerField(
        choices=[
            [1, 'Les femmes d’Alger (Picasso)'],
            [2, 'Three Studies of Lucian Freud (Bacon)'],
            [3, 'Der Schrei (Munch)'],
            [4, 'Sonnenblumen (van Gogh)'], ],
        widget=widgets.RadioSelect()
    )

    KnowG26 = models.IntegerField(
        choices=[
            [1, 'George Clooney'],
            [2, 'Jack Nicholson'],
            [3, 'Leonardo DiCaprio'],
            [4, 'Matthew McConaughey'], ],
        widget=widgets.RadioSelect()
    )

    KnowG27 = models.IntegerField(
        choices=[
            [1, 'New York'],
            [2, 'Paris'],
            [3, 'Prag'],
            [4, 'London'], ],
        widget=widgets.RadioSelect()
    )

    KnowG28 = models.IntegerField(
        choices=[
            [1, 'Kiefer'],
            [2, 'Seerose'],
            [3, 'Bambus'],
            [4, 'Reis'], ],
        widget=widgets.RadioSelect()
    )

    KnowG29 = models.IntegerField(
        choices=[
            [1, 'Max Liebermann'],
            [2, 'Paul Cézanne'],
            [3, 'Wassily Kandinsky'],
            [4, 'Édouard Manet'], ],
        widget=widgets.RadioSelect()
    )

    KnowG30 = models.IntegerField(
        choices=[
            [1, 'Vanessa'],
            [2, 'Sandy'],
            [3, 'Indira'],
            [4, 'Jessica'], ],
        widget=widgets.RadioSelect()
    )

    resultKnowGplayer = models.IntegerField()

    def set_KnowGplayer(self):
        self.resultKnowGplayer = self.group.resultKnowG

    eq1 = models.IntegerField(
        choices=[
            [1, 'Trifft überhaupt nicht zu'],
            [2, 'Trifft nicht zu'],
            [3, 'Trifft eher nicht zu'],
            [4, 'Teils-teils'],
            [5, 'Trifft eher zu'],
            [6, 'Trifft zu'],
            [7, 'Trifft sehr zu'], ],
    )
    eq2 = models.IntegerField(
        choices=[
            [1, 'Trifft überhaupt nicht zu'],
            [2, 'Trifft nicht zu'],
            [3, 'Trifft eher nicht zu'],
            [4, 'Teils-teils'],
            [5, 'Trifft eher zu'],
            [6, 'Trifft zu'],
            [7, 'Trifft sehr zu'], ],
    )
    eq3 = models.IntegerField(
        choices=[
            [1, 'Trifft überhaupt nicht zu'],
            [2, 'Trifft nicht zu'],
            [3, 'Trifft eher nicht zu'],
            [4, 'Teils-teils'],
            [5, 'Trifft eher zu'],
            [6, 'Trifft zu'],
            [7, 'Trifft sehr zu'], ],
    )
    eq4 = models.IntegerField(
        choices=[
            [1, 'Trifft überhaupt nicht zu'],
            [2, 'Trifft nicht zu'],
            [3, 'Trifft eher nicht zu'],
            [4, 'Teils-teils'],
            [5, 'Trifft eher zu'],
            [6, 'Trifft zu'],
            [7, 'Trifft sehr zu'], ],
    )
    eq5 = models.IntegerField(
        choices=[
            [1, 'Trifft überhaupt nicht zu'],
            [2, 'Trifft nicht zu'],
            [3, 'Trifft eher nicht zu'],
            [4, 'Teils-teils'],
            [5, 'Trifft eher zu'],
            [6, 'Trifft zu'],
            [7, 'Trifft sehr zu'], ],
    )
    eq6 = models.IntegerField(
        choices=[
            [1, 'Trifft überhaupt nicht zu'],
            [2, 'Trifft nicht zu'],
            [3, 'Trifft eher nicht zu'],
            [4, 'Teils-teils'],
            [5, 'Trifft eher zu'],
            [6, 'Trifft zu'],
            [7, 'Trifft sehr zu'], ],
    )
    eq7 = models.IntegerField(
        choices=[
            [1, 'Trifft überhaupt nicht zu'],
            [2, 'Trifft nicht zu'],
            [3, 'Trifft eher nicht zu'],
            [4, 'Teils-teils'],
            [5, 'Trifft eher zu'],
            [6, 'Trifft zu'],
            [7, 'Trifft sehr zu'], ],
    )
    eq8 = models.IntegerField(
        choices=[
            [1, 'Trifft überhaupt nicht zu'],
            [2, 'Trifft nicht zu'],
            [3, 'Trifft eher nicht zu'],
            [4, 'Teils-teils'],
            [5, 'Trifft eher zu'],
            [6, 'Trifft zu'],
            [7, 'Trifft sehr zu'], ],
    )
    eq9 = models.IntegerField(
        choices=[
            [1, 'Trifft überhaupt nicht zu'],
            [2, 'Trifft nicht zu'],
            [3, 'Trifft eher nicht zu'],
            [4, 'Teils-teils'],
            [5, 'Trifft eher zu'],
            [6, 'Trifft zu'],
            [7, 'Trifft sehr zu'], ],
    )
    eq10 = models.IntegerField(
        choices=[
            [1, 'Trifft überhaupt nicht zu'],
            [2, 'Trifft nicht zu'],
            [3, 'Trifft eher nicht zu'],
            [4, 'Teils-teils'],
            [5, 'Trifft eher zu'],
            [6, 'Trifft zu'],
            [7, 'Trifft sehr zu'], ],
    )
    eq11 = models.IntegerField(
        choices=[
            [1, 'Trifft überhaupt nicht zu'],
            [2, 'Trifft nicht zu'],
            [3, 'Trifft eher nicht zu'],
            [4, 'Teils-teils'],
            [5, 'Trifft eher zu'],
            [6, 'Trifft zu'],
            [7, 'Trifft sehr zu'], ],
    )
    eq12 = models.IntegerField(
        choices=[
            [1, 'Trifft überhaupt nicht zu'],
            [2, 'Trifft nicht zu'],
            [3, 'Trifft eher nicht zu'],
            [4, 'Teils-teils'],
            [5, 'Trifft eher zu'],
            [6, 'Trifft zu'],
            [7, 'Trifft sehr zu'], ],
    )
    eq13 = models.IntegerField(
        choices=[
            [1, 'Trifft überhaupt nicht zu'],
            [2, 'Trifft nicht zu'],
            [3, 'Trifft eher nicht zu'],
            [4, 'Teils-teils'],
            [5, 'Trifft eher zu'],
            [6, 'Trifft zu'],
            [7, 'Trifft sehr zu'], ],
    )
    eq14 = models.IntegerField(
        choices=[
            [1, 'Trifft überhaupt nicht zu'],
            [2, 'Trifft nicht zu'],
            [3, 'Trifft eher nicht zu'],
            [4, 'Teils-teils'],
            [5, 'Trifft eher zu'],
            [6, 'Trifft zu'],
            [7, 'Trifft sehr zu'], ],
    )
    eq15 = models.IntegerField(
        choices=[
            [1, 'Trifft überhaupt nicht zu'],
            [2, 'Trifft nicht zu'],
            [3, 'Trifft eher nicht zu'],
            [4, 'Teils-teils'],
            [5, 'Trifft eher zu'],
            [6, 'Trifft zu'],
            [7, 'Trifft sehr zu'], ],
    )
    eq16 = models.IntegerField(
        choices=[
            [1, 'Trifft überhaupt nicht zu'],
            [2, 'Trifft nicht zu'],
            [3, 'Trifft eher nicht zu'],
            [4, 'Teils-teils'],
            [5, 'Trifft eher zu'],
            [6, 'Trifft zu'],
            [7, 'Trifft sehr zu'], ],
    )

    resultEQ = models.IntegerField()

    def set_eqsum(self):

        self.resultEQ = 0

        self.resultEQ = sum(
            [self.eq1, self.eq2, self.eq3, self.eq4, self.eq5, self.eq6, self.eq7, self.eq8, self.eq9, self.eq10,
             self.eq11, self.eq12, self.eq13, self.eq14, self.eq15, self.eq16])

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
    stud = models.CharField(max_length=255)
    stru = models.IntegerField(
        choices=[
            [1, 'Ja'],
            [2, 'Nein'], ],
        widget=widgets.RadioSelect()
    )
    stru2 = models.IntegerField(
        choices=[
            [1, 'Allgemeine Wissensfragen'],
            [2, 'Mathematik'],
            [3, 'Worträtsel'],
            [4, 'Muster erkennen'],
            [5, 'Versteckte Formen'],
            [6, 'Emotionen im Team'],
            [7, 'Allgemeine Wissensfragen in Gruppen'],
            [8, 'Ich hatte nicht Schwierigkeiten irgendeinen Teil dieses Experiments zu verstehen'], ]
    )
    stru3 = models.IntegerField(
        choices=[
            [1, 'Ja'],
            [2, 'Nein'],
            [3, 'Ich hatte nicht Schwierigkeiten irgendeinen Teil dieses Experiments zu verstehen'], ],
        widget=widgets.RadioSelect()
    )
    dif1 = models.IntegerField(
        choices=[
            [1, 'Sehr leicht'],
            [2, 'Leicht'],
            [3, 'Eher leicht'],
            [4, 'Teils-teils'],
            [5, 'Eher schwer'],
            [6, 'Schwer'],
            [7, 'Sehr schwer'], ],
    )
    dif2 = models.IntegerField(
        choices=[
            [1, 'Sehr leicht'],
            [2, 'Leicht'],
            [3, 'Eher leicht'],
            [4, 'Teils-teils'],
            [5, 'Eher schwer'],
            [6, 'Schwer'],
            [7, 'Sehr schwer'], ],
    )
    dif3 = models.IntegerField(
        choices=[
            [1, 'Sehr leicht'],
            [2, 'Leicht'],
            [3, 'Eher leicht'],
            [4, 'Teils-teils'],
            [5, 'Eher schwer'],
            [6, 'Schwer'],
            [7, 'Sehr schwer'], ],
    )
    dif4 = models.IntegerField(
        choices=[
            [1, 'Sehr leicht'],
            [2, 'Leicht'],
            [3, 'Eher leicht'],
            [4, 'Teils-teils'],
            [5, 'Eher schwer'],
            [6, 'Schwer'],
            [7, 'Sehr schwer'], ],
    )
    dif5 = models.IntegerField(
        choices=[
            [1, 'Sehr leicht'],
            [2, 'Leicht'],
            [3, 'Eher leicht'],
            [4, 'Teils-teils'],
            [5, 'Eher schwer'],
            [6, 'Schwer'],
            [7, 'Sehr schwer'], ],
    )
    dif6 = models.IntegerField(
        choices=[
            [1, 'Sehr leicht'],
            [2, 'Leicht'],
            [3, 'Eher leicht'],
            [4, 'Teils-teils'],
            [5, 'Eher schwer'],
            [6, 'Schwer'],
            [7, 'Sehr schwer'], ],
    )
    dif7 = models.IntegerField(
        choices=[
            [1, 'Sehr leicht'],
            [2, 'Leicht'],
            [3, 'Eher leicht'],
            [4, 'Teils-teils'],
            [5, 'Eher schwer'],
            [6, 'Schwer'],
            [7, 'Sehr schwer'], ],
    )

    estimate1 = models.PositiveIntegerField(validators=[MaxValueValidator(100)])
    estimate2 = models.PositiveIntegerField(validators=[MaxValueValidator(100)])
    estimate3 = models.PositiveIntegerField(validators=[MaxValueValidator(100)])
    estimate4 = models.PositiveIntegerField(validators=[MaxValueValidator(100)])
    estimate5 = models.PositiveIntegerField(validators=[MaxValueValidator(100)])
    estimate6 = models.PositiveIntegerField(validators=[MaxValueValidator(100)])
    estimate7 = models.PositiveIntegerField(validators=[MaxValueValidator(100)])

    estimate1paydist = models.CurrencyField()
    estimate2paydist = models.CurrencyField()
    estimate3paydist = models.CurrencyField()
    estimate4paydist = models.CurrencyField()
    estimate5paydist = models.CurrencyField()
    estimate6paydist = models.CurrencyField()
    estimate7paydist = models.CurrencyField()

    belief1 = models.PositiveIntegerField(validators=[MaxValueValidator(100)])
    belief2 = models.PositiveIntegerField(validators=[MaxValueValidator(100)])
    belief3 = models.PositiveIntegerField(validators=[MaxValueValidator(100)])
    belief4 = models.PositiveIntegerField(validators=[MaxValueValidator(100)])
    belief5 = models.PositiveIntegerField(validators=[MaxValueValidator(100)])
    belief6 = models.PositiveIntegerField(validators=[MaxValueValidator(100)])
    belief7 = models.PositiveIntegerField(validators=[MaxValueValidator(100)])

    belief1paydist = models.CurrencyField()
    belief2paydist = models.CurrencyField()
    belief3paydist = models.CurrencyField()
    belief4paydist = models.CurrencyField()
    belief5paydist = models.CurrencyField()
    belief6paydist = models.CurrencyField()
    belief7paydist = models.CurrencyField()

    groupbelief1 = models.PositiveIntegerField(validators=[MaxValueValidator(30)])
    groupbelief2 = models.PositiveIntegerField(validators=[MaxValueValidator(100)])
    groupbelief3 = models.PositiveIntegerField(validators=[MaxValueValidator(30)])
    groupbelief4 = models.PositiveIntegerField(validators=[MaxValueValidator(30)])

    cor1 = models.PositiveIntegerField(validators=[MaxValueValidator(100)])
    cor2 = models.PositiveIntegerField(validators=[MaxValueValidator(100)])
    cor3 = models.PositiveIntegerField(validators=[MaxValueValidator(100)])
    cor4 = models.PositiveIntegerField(validators=[MaxValueValidator(100)])
    cor5 = models.PositiveIntegerField(validators=[MaxValueValidator(100)])
    cor6 = models.PositiveIntegerField(validators=[MaxValueValidator(100)])
    cor7 = models.PositiveIntegerField(validators=[MaxValueValidator(100)])
    cor8 = models.PositiveIntegerField(validators=[MaxValueValidator(100)])


    def trans_nones(self):

        if self.resultKnowS is None:
            self.resultKnowS = 0

        if self.resultSumming is None:
            self.resultSumming = 0

        if self.counterWordsall is None:
            self.counterWordsall = 0

        if self.failuresWordsall is None:
            self.failuresWordsall = 0

        if self.resultMat is None:
            self.resultMat = 0

        if self.resultFig is None:
            self.resultFig = 0

        if self.resultEQ is None:
            self.resultEQ = 0

        if self.resultKnowGplayer is None:
            self.resultKnowGplayer = 0

        if self.resultWordsall is None:
            self.resultWordsall = 0

    def set_estimatepaydist(self):

        self.estimate1paydist = 1.5 * (1 - (((self.subsession.p_male_better1 - self.estimate1) / 100) ** 2))

        self.estimate2paydist = 1.5 * (1 - (((self.subsession.p_male_better2 - self.estimate2) / 100) ** 2))

        self.estimate3paydist = 1.5 * (1 - (((self.subsession.p_male_better3 - self.estimate3) / 100) ** 2))

        self.estimate4paydist = 1.5 * (1 - (((self.subsession.p_male_better4 - self.estimate4) / 100) ** 2))

        self.estimate5paydist = 1.5 * (1 - (((self.subsession.p_male_better5 - self.estimate5) / 100) ** 2))

        self.estimate6paydist = 1.5 * (1 - (((self.subsession.p_male_better6 - self.estimate6) / 100) ** 2))

        self.estimate7paydist = 1.5 * (1 - (((self.subsession.p_male_better7 - self.estimate7) / 100) ** 2))

    def set_beliefpaydist(self):

        all_players = self.subsession.get_players()

        all_estimate1 = [p.estimate1 for p in all_players
                         if p is not self]

        averagewithoutself1 = int(sum(all_estimate1) / len(all_estimate1))

        self.belief1paydist = 1.5 * (1 - ((averagewithoutself1 - self.belief1) / 100) ** 2)

        all_estimate2 = [p.estimate2 for p in all_players
                         if p is not self]

        averagewithoutself2 = int(sum(all_estimate2) / len(all_estimate2))

        self.belief2paydist = 1.5 * (1 - ((averagewithoutself2 - self.belief2) / 100) ** 2)

        all_estimate3 = [p.estimate3 for p in all_players
                         if p is not self]

        averagewithoutself3 = int(sum(all_estimate3) / len(all_estimate3))

        self.belief3paydist = 1.5 * (1 - ((averagewithoutself3 - self.belief3) / 100) ** 2)

        all_estimate4 = [p.estimate3 for p in all_players
                         if p is not self]

        averagewithoutself4 = int(sum(all_estimate4) / len(all_estimate4))

        self.belief4paydist = 1.5 * (1 - ((averagewithoutself4 - self.belief4) / 100) ** 2)

        all_estimate5 = [p.estimate5 for p in all_players
                         if p is not self]

        averagewithoutself5 = int(sum(all_estimate5) / len(all_estimate5))

        self.belief5paydist = 1.5 * (1 - ((averagewithoutself5 - self.belief5) / 100) ** 2)

        all_estimate6 = [p.estimate6 for p in all_players
                         if p is not self]

        averagewithoutself6 = int(sum(all_estimate6) / len(all_estimate6))

        self.belief6paydist = 1.5 * (1 - ((averagewithoutself6 - self.belief6) / 100) ** 2)

        all_estimate7 = [p.estimate7 for p in all_players
                         if p is not self]

        averagewithoutself7 = int(sum(all_estimate7) / len(all_estimate7))

        self.belief7paydist = 1.5 * (1 - ((averagewithoutself7 - self.belief7) / 100) ** 2)

    payoff_1_5 = models.CurrencyField()
    payoff_1_5_label = models.CharField(max_length=255)
    payoff7 = models.CurrencyField()
    payoff8sum = models.CurrencyField()
    payoff7and8sum = models.CurrencyField()
    randompick = models.IntegerField()
    payofftotal = models.CurrencyField()
    res = models.IntegerField()

    def set_payoffs(self):

        self.payoff7 = self.resultKnowGplayer * Constants.pointsKnowG
        payoff81 = random.choice(
            [self.estimate1paydist, self.estimate2paydist, self.estimate3paydist, self.estimate4paydist,
             self.estimate5paydist, self.estimate6paydist, self.estimate7paydist])
        payoff82 = random.choice(
            [self.belief1paydist, self.belief2paydist, self.belief3paydist, self.belief4paydist, self.belief5paydist,
             self.belief6paydist, self.belief7paydist])
        self.payoff8sum = payoff81 + payoff82
        self.payoff7and8sum = self.payoff7 + self.payoff8sum

        self.randompick = random.randint(1, 5)
        resultlist = [self.resultKnowS, self.resultSumming, self.resultWordsall, self.resultMat, self.resultFig]
        pointslist = [Constants.pointsKnowS, Constants.pointsSumming, Constants.pointsWord, Constants.pointsMat,
                      Constants.pointsFig]
        if self.randompick != 3:
            self.res = resultlist[self.randompick-1]
            pts = pointslist[self.randompick-1]

            self.payoff_1_5 = self.res * pts
            self.payoff_1_5_label = Constants.tasklist[self.randompick-1]

            self.payofftotal = self.payoff_1_5 + self.payoff8sum + self.payoff7 + c(5)
        elif self.randompick == 3:
            self.payoff_1_5_label = Constants.tasklist[self.randompick - 1]
            self.res = self.resultWordsall
            self.payoff_1_5 = self.res * Constants.pointsWord
            self.payofftotal = self.payoff_1_5 + self.payoff8sum + self.payoff7 + c(5)

        self.payoff = self.payofftotal - c(5)
