from otree.api import Currency as c, currency_range
from otreeutils.pages import ExtendedPage
from . import models
from ._builtin import Page, WaitPage
from .models import Constants
import time
import random

class BasePage1(Page):
    def get_timeout_seconds(self):
        return self.session.vars['expiry_timestamp_1'] - time.time()
    def is_displayed(self):
        return self.session.vars['expiry_timestamp_1'] - time.time() > 3
    timer_text = 'Verbleibende Zeit für alle Teilaufgaben (Danach werden Sie automatisch weitergeleitet):'

class BasePage2(Page):
    def get_timeout_seconds(self):
        return self.session.vars['expiry_timestamp_2'] - time.time()
    def is_displayed(self):
        return self.session.vars['expiry_timestamp_2'] - time.time() > 3
    timer_text = 'Verbleibende Zeit für alle Teilaufgaben (Danach werden Sie automatisch weitergeleitet):'

class BasePage3(Page):
    def get_timeout_seconds(self):
        return self.session.vars['expiry_timestamp_3'] - time.time()
    def is_displayed(self):
        return self.session.vars['expiry_timestamp_3'] - time.time() > 3
    timer_text = 'Verbleibende Zeit für alle Teilaufgaben (Danach werden Sie automatisch weitergeleitet):'

class BasePage5(Page):
    def get_timeout_seconds(self):
        return self.session.vars['expiry_timestamp_5'] - time.time()
    def is_displayed(self):
        return self.session.vars['expiry_timestamp_5'] - time.time() > 3
    timer_text = 'Verbleibende Zeit für diese Teilaufgabe (Danach werden Sie automatisch weitergeleitet):'

class BasePage6(Page):
    def get_timeout_seconds(self):
        return self.session.vars['expiry_timestamp_6'] - time.time()
    def is_displayed(self):
        return self.session.vars['expiry_timestamp_6'] - time.time() > 3
    timer_text = 'Verbleibende Zeit für diese Teilaufgabe (Danach werden Sie automatisch weitergeleitet):'

class BasePage7(Page):
    def get_timeout_seconds(self):
        return self.session.vars['expiry_timestamp_7'] - time.time()
    def is_displayed(self):
        return self.session.vars['expiry_timestamp_7'] - time.time() > 3
    timer_text = 'Verbleibende Zeit für diese Teilaufgabe (Danach werden Sie automatisch weitergeleitet):'

class BasePage8(Page):
    def get_timeout_seconds(self):
        return self.session.vars['expiry_timestamp_8'] - time.time()
    def is_displayed(self):
        return self.session.vars['expiry_timestamp_8'] - time.time() > 3
    timer_text = 'Verbleibende Zeit für alle Teilaufgaben (Danach werden Sie automatisch weitergeleitet):'

class BasePage9(Page):
    def get_timeout_seconds(self):
        return self.session.vars['expiry_timestamp_9'] - time.time()
    def is_displayed(self):
        return self.session.vars['expiry_timestamp_9'] - time.time() > 3
    timer_text = 'Verbleibende Zeit für alle Teilaufgaben (Danach werden Sie automatisch weitergeleitet):'


class AGeneralIntro(Page):
    pass

class WaitIntro(WaitPage):
    wait_for_all_groups = True


class KnowSInstr(ExtendedPage):
    timeout_warning_seconds = 120
    timeout_warning_message = 'Bitte beeilen Sie sich, die Zeit ist um.'


class WaitKnowS(WaitPage):
    wait_for_all_groups = True
    def after_all_players_arrive(self):
        self.session.vars['expiry_timestamp_8'] = time.time() + Constants.timeKnowS

class KnowS1(BasePage8):
    form_model = models.Player
    form_fields = ['KnowS1']
    def before_next_page(self):
        self.player.set_feedb_KnowS()

class KnowS2(BasePage8):
    form_model = models.Player
    form_fields = ['KnowS2']
    def before_next_page(self):
        self.player.set_feedb_KnowS()

class KnowS3(BasePage8):
    form_model = models.Player
    form_fields = ['KnowS3']
    def before_next_page(self):
        self.player.set_feedb_KnowS()

class KnowS4(BasePage8):
    form_model = models.Player
    form_fields = ['KnowS4']
    def before_next_page(self):
        self.player.set_feedb_KnowS()

class KnowS5(BasePage8):
    form_model = models.Player
    form_fields = ['KnowS5']
    def before_next_page(self):
        self.player.set_feedb_KnowS()

class KnowS6(BasePage8):
    form_model = models.Player
    form_fields = ['KnowS6']
    def before_next_page(self):
        self.player.set_feedb_KnowS()

class KnowS7(BasePage8):
    form_model = models.Player
    form_fields = ['KnowS7']
    def before_next_page(self):
        self.player.set_feedb_KnowS()

class KnowS8(BasePage8):
    form_model = models.Player
    form_fields = ['KnowS8']
    def before_next_page(self):
        self.player.set_feedb_KnowS()

class KnowS9(BasePage8):
    form_model = models.Player
    form_fields = ['KnowS9']
    def before_next_page(self):
        self.player.set_feedb_KnowS()

class KnowS10(BasePage8):
    form_model = models.Player
    form_fields = ['KnowS10']
    def before_next_page(self):
        self.player.set_feedb_KnowS()

class KnowS11(BasePage8):
    form_model = models.Player
    form_fields = ['KnowS11']
    def before_next_page(self):
        self.player.set_feedb_KnowS()

class KnowS12(BasePage8):
    form_model = models.Player
    form_fields = ['KnowS12']
    def before_next_page(self):
        self.player.set_feedb_KnowS()

class KnowS13(BasePage8):
    form_model = models.Player
    form_fields = ['KnowS13']
    def before_next_page(self):
        self.player.set_feedb_KnowS()

class KnowS14(BasePage8):
    form_model = models.Player
    form_fields = ['KnowS14']
    def before_next_page(self):
        self.player.set_feedb_KnowS()

class KnowS15(BasePage8):
    form_model = models.Player
    form_fields = ['KnowS15']
    def before_next_page(self):
        self.player.set_feedb_KnowS()

class KnowS16(BasePage8):
    form_model = models.Player
    form_fields = ['KnowS16']
    def before_next_page(self):
        self.player.set_feedb_KnowS()

class KnowS17(BasePage8):
    form_model = models.Player
    form_fields = ['KnowS17']
    def before_next_page(self):
        self.player.set_feedb_KnowS()

class KnowS18(BasePage8):
    form_model = models.Player
    form_fields = ['KnowS18']
    def before_next_page(self):
        self.player.set_feedb_KnowS()

class KnowS19(BasePage8):
    form_model = models.Player
    form_fields = ['KnowS19']
    def before_next_page(self):
        self.player.set_feedb_KnowS()

class KnowS20(BasePage8):
    form_model = models.Player
    form_fields = ['KnowS20']
    def before_next_page(self):
        self.player.set_feedb_KnowS()

class KnowS21(BasePage8):
    form_model = models.Player
    form_fields = ['KnowS21']
    def before_next_page(self):
        self.player.set_feedb_KnowS()

class KnowS22(BasePage8):
    form_model = models.Player
    form_fields = ['KnowS22']
    def before_next_page(self):
        self.player.set_feedb_KnowS()

class KnowS23(BasePage8):
    form_model = models.Player
    form_fields = ['KnowS23']
    def before_next_page(self):
        self.player.set_feedb_KnowS()

class KnowS24(BasePage8):
    form_model = models.Player
    form_fields = ['KnowS24']
    def before_next_page(self):
        self.player.set_feedb_KnowS()

class KnowS25(BasePage8):
    form_model = models.Player
    form_fields = ['KnowS25']
    def before_next_page(self):
        self.player.set_feedb_KnowS()

class KnowS26(BasePage8):
    form_model = models.Player
    form_fields = ['KnowS26']
    def before_next_page(self):
        self.player.set_feedb_KnowS()

class KnowS27(BasePage8):
    form_model = models.Player
    form_fields = ['KnowS27']
    def before_next_page(self):
        self.player.set_feedb_KnowS()

class KnowS28(BasePage8):
    form_model = models.Player
    form_fields = ['KnowS28']
    def before_next_page(self):
        self.player.set_feedb_KnowS()

class KnowS29(BasePage8):
    form_model = models.Player
    form_fields = ['KnowS29']
    def before_next_page(self):
        self.player.set_feedb_KnowS()

class KnowS30(BasePage8):
    form_model = models.Player
    form_fields = ['KnowS30']
    def before_next_page(self):
        self.player.set_feedb_KnowS()

class WaitKnowS2(WaitPage):
    wait_for_all_groups = True


class SummingInstr(ExtendedPage):
    timeout_warning_seconds = 100
    timeout_warning_message = 'Bitte beeilen Sie sich, die Zeit ist um.'


class WaitSumming(WaitPage):
    wait_for_all_groups = True
    def after_all_players_arrive(self):
        self.session.vars['expiry_timestamp_1'] = time.time() + Constants.timeSumming

class Summing1(BasePage1):
    form_model = models.Player
    form_fields = ['Summing1']
    def before_next_page(self):
        self.player.set_feedb_Summing()

class Summing2(BasePage1):
    form_model = models.Player
    form_fields = ['Summing2']
    def before_next_page(self):
        self.player.set_feedb_Summing()

class Summing3(BasePage1):
    form_model = models.Player
    form_fields = ['Summing3']
    def before_next_page(self):
        self.player.set_feedb_Summing()

class Summing4(BasePage1):
    form_model = models.Player
    form_fields = ['Summing4']
    def before_next_page(self):
        self.player.set_feedb_Summing()

class Summing5(BasePage1):
    form_model = models.Player
    form_fields = ['Summing5']
    def before_next_page(self):
        self.player.set_feedb_Summing()

class Summing6(BasePage1):
    form_model = models.Player
    form_fields = ['Summing6']
    def before_next_page(self):
        self.player.set_feedb_Summing()

class Summing7(BasePage1):
    form_model = models.Player
    form_fields = ['Summing7']
    def before_next_page(self):
        self.player.set_feedb_Summing()

class Summing8(BasePage1):
    form_model = models.Player
    form_fields = ['Summing8']
    def before_next_page(self):
        self.player.set_feedb_Summing()

class Summing9(BasePage1):
    form_model = models.Player
    form_fields = ['Summing9']
    def before_next_page(self):
        self.player.set_feedb_Summing()

class Summing10(BasePage1):
    form_model = models.Player
    form_fields = ['Summing10']
    def before_next_page(self):
        self.player.set_feedb_Summing()

class Summing11(BasePage1):
    form_model = models.Player
    form_fields = ['Summing11']
    def before_next_page(self):
        self.player.set_feedb_Summing()

class Summing12(BasePage1):
    form_model = models.Player
    form_fields = ['Summing12']
    def before_next_page(self):
        self.player.set_feedb_Summing()

class Summing13(BasePage1):
    form_model = models.Player
    form_fields = ['Summing13']
    def before_next_page(self):
        self.player.set_feedb_Summing()

class Summing14(BasePage1):
    form_model = models.Player
    form_fields = ['Summing14']
    def before_next_page(self):
        self.player.set_feedb_Summing()

class Summing15(BasePage1):
    form_model = models.Player
    form_fields = ['Summing15']
    def before_next_page(self):
        self.player.set_feedb_Summing()

class Summing16(BasePage1):
    form_model = models.Player
    form_fields = ['Summing16']
    def before_next_page(self):
        self.player.set_feedb_Summing()

class Summing17(BasePage1):
    form_model = models.Player
    form_fields = ['Summing17']
    def before_next_page(self):
        self.player.set_feedb_Summing()

class Summing18(BasePage1):
    form_model = models.Player
    form_fields = ['Summing18']
    def before_next_page(self):
        self.player.set_feedb_Summing()

class Summing19(BasePage1):
    form_model = models.Player
    form_fields = ['Summing19']
    def before_next_page(self):
        self.player.set_feedb_Summing()

class Summing20(BasePage1):
    form_model = models.Player
    form_fields = ['Summing20']
    def before_next_page(self):
        self.player.set_feedb_Summing()

class Summing21(BasePage1):
    form_model = models.Player
    form_fields = ['Summing21']
    def before_next_page(self):
        self.player.set_feedb_Summing()

class Summing22(BasePage1):
    form_model = models.Player
    form_fields = ['Summing22']
    def before_next_page(self):
        self.player.set_feedb_Summing()

class Summing23(BasePage1):
    form_model = models.Player
    form_fields = ['Summing23']
    def before_next_page(self):
        self.player.set_feedb_Summing()

class Summing24(BasePage1):
    form_model = models.Player
    form_fields = ['Summing24']
    def before_next_page(self):
        self.player.set_feedb_Summing()

class Summing25(BasePage1):
    form_model = models.Player
    form_fields = ['Summing25']
    def before_next_page(self):
        self.player.set_feedb_Summing()

class Summing26(BasePage1):
    form_model = models.Player
    form_fields = ['Summing26']
    def before_next_page(self):
        self.player.set_feedb_Summing()

class Summing27(BasePage1):
    form_model = models.Player
    form_fields = ['Summing27']
    def before_next_page(self):
        self.player.set_feedb_Summing()

class Summing28(BasePage1):
    form_model = models.Player
    form_fields = ['Summing28']
    def before_next_page(self):
        self.player.set_feedb_Summing()

class Summing29(BasePage1):
    form_model = models.Player
    form_fields = ['Summing29']
    def before_next_page(self):
        self.player.set_feedb_Summing()

class Summing30(BasePage1):
    form_model = models.Player
    form_fields = ['Summing30']
    def before_next_page(self):
        self.player.set_feedb_Summing()

class WaitSumming2(WaitPage):
    wait_for_all_groups = True

class WordInstr(ExtendedPage):
    timeout_warning_seconds = 180
    timeout_warning_message = 'Bitte beeilen Sie sich, die Zeit ist um.'



class WaitWord1(WaitPage):
    wait_for_all_groups = True
    def after_all_players_arrive(self):
        self.session.vars['expiry_timestamp_5'] = time.time() + Constants.timeWord1

class Word1(BasePage5):
    form_model = models.Player
    form_fields = ['word{}'.format(i) for i in range(1, 31)]
    def before_next_page(self):
        self.player.count_1()
        self.player.word1 = 0
        self.player.word2 = 0
        self.player.word3 = 0
        self.player.word4 = 0
        self.player.word5 = 0
        self.player.word6 = 0
        self.player.word7 = 0
        self.player.word8 = 0
        self.player.word9 = 0
        self.player.word10 = 0
        self.player.word11 = 0
        self.player.word12 = 0
        self.player.word13 = 0
        self.player.word14 = 0
        self.player.word15 = 0
        self.player.word16 = 0
        self.player.word17 = 0
        self.player.word18 = 0
        self.player.word19 = 0
        self.player.word20 = 0
        self.player.word21 = 0
        self.player.word22 = 0
        self.player.word23 = 0
        self.player.word24 = 0
        self.player.word25 = 0
        self.player.word26 = 0
        self.player.word27 = 0
        self.player.word28 = 0
        self.player.word29 = 0
        self.player.word30 = 0

class WaitWord2(WaitPage):
    wait_for_all_groups = True
    def after_all_players_arrive(self):
        self.session.vars['expiry_timestamp_6'] = time.time() + Constants.timeWord2

class Word2(BasePage6):
    form_model = models.Player
    form_fields = ['word{}'.format(i) for i in range(1, 31)]
    def before_next_page(self):
        self.player.count_2()
        self.player.word1 = 0
        self.player.word2 = 0
        self.player.word3 = 0
        self.player.word4 = 0
        self.player.word5 = 0
        self.player.word6 = 0
        self.player.word7 = 0
        self.player.word8 = 0
        self.player.word9 = 0
        self.player.word10 = 0
        self.player.word11 = 0
        self.player.word12 = 0
        self.player.word13 = 0
        self.player.word14 = 0
        self.player.word15 = 0
        self.player.word16 = 0
        self.player.word17 = 0
        self.player.word18 = 0
        self.player.word19 = 0
        self.player.word20 = 0
        self.player.word21 = 0
        self.player.word22 = 0
        self.player.word23 = 0
        self.player.word24 = 0
        self.player.word25 = 0
        self.player.word26 = 0
        self.player.word27 = 0
        self.player.word28 = 0
        self.player.word29 = 0
        self.player.word30 = 0

class WaitWord3(WaitPage):
    wait_for_all_groups = True
    def after_all_players_arrive(self):
        self.session.vars['expiry_timestamp_7'] = time.time() + Constants.timeWord3

class WaitWord4(WaitPage):
    wait_for_all_groups = True

class Word3(BasePage7):
    form_model = models.Player
    form_fields = ['word{}'.format(i) for i in range(1, 31)]
    def before_next_page(self):
        self.player.count_3()
        self.player.count_all()

class MatInstr(ExtendedPage):
    timeout_warning_seconds = 180
    timeout_warning_message = 'Bitte beeilen Sie sich, die Zeit ist um.'

class Mat1(BasePage3):
    form_model = models.Player
    form_fields = ['Mat1']
    def before_next_page(self):
        self.player.set_feedb_Mat()

class Mat2(BasePage3):
    form_model = models.Player
    form_fields = ['Mat2']
    def before_next_page(self):
        self.player.set_feedb_Mat()

class Mat3(BasePage3):
    form_model = models.Player
    form_fields = ['Mat3']
    def before_next_page(self):
        self.player.set_feedb_Mat()

class Mat4(BasePage3):
    form_model = models.Player
    form_fields = ['Mat4']
    def before_next_page(self):
        self.player.set_feedb_Mat()

class Mat5(BasePage3):
    form_model = models.Player
    form_fields = ['Mat5']
    def before_next_page(self):
        self.player.set_feedb_Mat()

class Mat6(BasePage3):
    form_model = models.Player
    form_fields = ['Mat6']
    def before_next_page(self):
        self.player.set_feedb_Mat()

class Mat7(BasePage3):
    form_model = models.Player
    form_fields = ['Mat7']
    def before_next_page(self):
        self.player.set_feedb_Mat()

class Mat8(BasePage3):
    form_model = models.Player
    form_fields = ['Mat8']
    def before_next_page(self):
        self.player.set_feedb_Mat()

class Mat9(BasePage3):
    form_model = models.Player
    form_fields = ['Mat9']
    def before_next_page(self):
        self.player.set_feedb_Mat()

class Mat10(BasePage3):
    form_model = models.Player
    form_fields = ['Mat10']
    def before_next_page(self):
        self.player.set_feedb_Mat()

class WaitMat(WaitPage):
    wait_for_all_groups = True


class WaitMat2(WaitPage):
    wait_for_all_groups = True
    def after_all_players_arrive(self):
        self.session.vars['expiry_timestamp_3'] = time.time() + Constants.timeMat

class FigInstr(ExtendedPage):
    timeout_warning_seconds = 120
    timeout_warning_message = 'Bitte beeilen Sie sich, die Zeit ist um.'

class WaitFig(WaitPage):
    wait_for_all_groups = True
    def after_all_players_arrive(self):
        self.session.vars['expiry_timestamp_9'] = time.time() + Constants.timeFig


class WaitFig2(WaitPage):
    wait_for_all_groups = True

class WaitEQ(WaitPage):
    wait_for_all_groups = True

class WaitEQ2(WaitPage):
    wait_for_all_groups = True

class Fig1(BasePage9):
    form_model = models.Player
    form_fields = ['Fig1']
    def before_next_page(self):
        self.player.set_feedb_Fig()

class Fig2(BasePage9):
    form_model = models.Player
    form_fields = ['Fig2']
    def before_next_page(self):
        self.player.set_feedb_Fig()

class Fig3(BasePage9):
    form_model = models.Player
    form_fields = ['Fig3']
    def before_next_page(self):
        self.player.set_feedb_Fig()

class Fig4(BasePage9):
    form_model = models.Player
    form_fields = ['Fig4']
    def before_next_page(self):
        self.player.set_feedb_Fig()

class Fig5(BasePage9):
    form_model = models.Player
    form_fields = ['Fig5']
    def before_next_page(self):
        self.player.set_feedb_Fig()


class Fig6(BasePage9):
    form_model = models.Player
    form_fields = ['Fig6']
    def before_next_page(self):
        self.player.set_feedb_Fig()


class Fig7(BasePage9):
    form_model = models.Player
    form_fields = ['Fig7']
    def before_next_page(self):
        self.player.set_feedb_Fig()


class Fig8(BasePage9):
    form_model = models.Player
    form_fields = ['Fig8']
    def before_next_page(self):
        self.player.set_feedb_Fig()


class Fig9(BasePage9):
    form_model = models.Player
    form_fields = ['Fig9']
    def before_next_page(self):
        self.player.set_feedb_Fig()

class Fig10(BasePage9):
    form_model = models.Player
    form_fields = ['Fig10']
    def before_next_page(self):
        self.player.set_feedb_Fig()

class EQInstr(ExtendedPage):
    timeout_warning_seconds = 120
    timeout_warning_message = 'Bitte beeilen Sie sich, die Zeit ist um.'

class EQ(ExtendedPage):
    form_model = models.Player
    form_fields = ['eq{}'.format(j) for j in range(1, 17)]
    def before_next_page(self):
        self.player.set_eqsum()
    timeout_warning_seconds = 300
    timeout_warning_message = 'Bitte beeilen Sie sich, die Zeit ist um.'

class KnowGInstr(ExtendedPage):
    def before_next_page(self):
        self.player.chat_nickname()
    timeout_warning_seconds = 180
    timeout_warning_message = 'Bitte beeilen Sie sich, die Zeit ist um.'

class WaitKnowG3(WaitPage):
    wait_for_all_groups = True
    def after_all_players_arrive(self):
        self.session.vars['expiry_timestamp_2'] = time.time() + Constants.timeKnowG

class WaitKnowG4(WaitPage):
    wait_for_all_groups = True

class KnowG1(BasePage2):
    form_model = models.Player
    form_fields = ['KnowG1']
class KnowG2(BasePage2):
    form_model = models.Player
    form_fields = ['KnowG2']
class KnowG3(BasePage2):
    form_model = models.Player
    form_fields = ['KnowG3']
class KnowG4(BasePage2):
    form_model = models.Player
    form_fields = ['KnowG4']
class KnowG5(BasePage2):
    form_model = models.Player
    form_fields = ['KnowG5']
class KnowG6(BasePage2):
    form_model = models.Player
    form_fields = ['KnowG6']
class KnowG7(BasePage2):
    form_model = models.Player
    form_fields = ['KnowG7']
class KnowG8(BasePage2):
    form_model = models.Player
    form_fields = ['KnowG8']
class KnowG9(BasePage2):
    form_model = models.Player
    form_fields = ['KnowG9']
class KnowG10(BasePage2):
    form_model = models.Player
    form_fields = ['KnowG10']
class KnowG11(BasePage2):
    form_model = models.Player
    form_fields = ['KnowG11']
class KnowG12(BasePage2):
    form_model = models.Player
    form_fields = ['KnowG12']
class KnowG13(BasePage2):
    form_model = models.Player
    form_fields = ['KnowG13']
class KnowG14(BasePage2):
    form_model = models.Player
    form_fields = ['KnowG14']
class KnowG15(BasePage2):
    form_model = models.Player
    form_fields = ['KnowG15']
class KnowG16(BasePage2):
    form_model = models.Player
    form_fields = ['KnowG16']
class KnowG17(BasePage2):
    form_model = models.Player
    form_fields = ['KnowG17']
class KnowG18(BasePage2):
    form_model = models.Player
    form_fields = ['KnowG18']
class KnowG19(BasePage2):
    form_model = models.Player
    form_fields = ['KnowG19']
class KnowG20(BasePage2):
    form_model = models.Player
    form_fields = ['KnowG20']
class KnowG21(BasePage2):
    form_model = models.Player
    form_fields = ['KnowG21']
class KnowG22(BasePage2):
    form_model = models.Player
    form_fields = ['KnowG22']
class KnowG23(BasePage2):
    form_model = models.Player
    form_fields = ['KnowG23']
class KnowG24(BasePage2):
    form_model = models.Player
    form_fields = ['KnowG24']
class KnowG25(BasePage2):
    form_model = models.Player
    form_fields = ['KnowG25']
class KnowG26(BasePage2):
    form_model = models.Player
    form_fields = ['KnowG26']
class KnowG27(BasePage2):
    form_model = models.Player
    form_fields = ['KnowG27']
class KnowG28(BasePage2):
    form_model = models.Player
    form_fields = ['KnowG28']
class KnowG29(BasePage2):
    form_model = models.Player
    form_fields = ['KnowG29']
class KnowG30(BasePage2):
    form_model = models.Player
    form_fields = ['KnowG30']

class WaitKnowG2(WaitPage):
    wait_for_all_groups = True

class Sur1(ExtendedPage):
    form_model = models.Player
    form_fields = ['age', 'gen', 'eng', 'stud', 'stru', 'stru2', 'stru3', 'dif1', 'dif2', 'dif3', 'dif4', 'dif5', 'dif6', 'dif7']
    def before_next_page(self):
        self.group.set_feedb_KnowGresult()
        self.player.set_KnowGplayer()
        self.player.trans_nones()
    timeout_warning_seconds = 180
    timeout_warning_message = 'Bitte beeilen Sie sich, die Zeit ist um.'

class WaitSur1(WaitPage):
    wait_for_all_groups = True
    def after_all_players_arrive(self):
        self.subsession.set_gendercomparisons()

class Sur2(ExtendedPage):
    form_model = models.Player
    form_fields = ['estimate1', 'estimate2','estimate3','estimate4','estimate5','estimate6','estimate7']
    def before_next_page(self):
        self.player.set_estimatepaydist()
    timeout_warning_seconds = 360
    timeout_warning_message = 'Bitte beeilen Sie sich, die Zeit ist um.'
class WaitSur2(WaitPage):
    wait_for_all_groups = True

class Sur3(ExtendedPage):
    form_model = models.Player
    form_fields = ['belief1', 'belief2', 'belief3', 'belief4', 'belief5', 'belief6', 'belief7']
    timeout_warning_seconds = 300
    timeout_warning_message = 'Bitte beeilen Sie sich, die Zeit ist um.'
    def before_next_page(self):
        self.player.set_beliefpaydist()
        self.player.set_payoffs()

class WaitSur3(WaitPage):
    wait_for_all_groups = True

class Sur4(ExtendedPage):
    form_model = models.Player
    form_fields = ['groupbelief1', 'groupbelief2']
    timeout_warning_seconds = 100
    timeout_warning_message = 'Bitte beeilen Sie sich, die Zeit ist um.'

class Sur5(ExtendedPage):
    form_model = models.Player
    form_fields = ['groupbelief3', 'groupbelief4']
    timeout_warning_seconds = 100
    timeout_warning_message = 'Bitte beeilen Sie sich, die Zeit ist um.'

class Sur6(ExtendedPage):
    form_model = models.Player
    form_fields = ['cor1', 'cor2','cor3', 'cor4','cor5', 'cor6','cor7', 'cor8']
    timeout_warning_seconds = 120
    timeout_warning_message = 'Bitte beeilen Sie sich, die Zeit ist um.'

class WaitSur4(WaitPage):
    wait_for_all_groups = True

class WaitSur5(WaitPage):
    wait_for_all_groups = True

class Outro(Page):
    pass

page_sequence = [
    AGeneralIntro,
    WaitIntro,
    KnowSInstr,
    WaitKnowS,
    KnowS1,
    KnowS2,
    KnowS3,
    KnowS4,
    KnowS5,
    KnowS6,
    KnowS7,
    KnowS8,
    KnowS9,
    KnowS10,
    KnowS11,
    KnowS12,
    KnowS13,
    KnowS14,
    KnowS15,
    KnowS16,
    KnowS17,
    KnowS18,
    KnowS19,
    KnowS20,
    KnowS21,
    KnowS22,
    KnowS23,
    KnowS24,
    KnowS25,
    KnowS26,
    KnowS27,
    KnowS28,
    KnowS29,
    KnowS30,
    WaitKnowS2,
    SummingInstr,
    WaitSumming,
    Summing1,
    Summing2,
    Summing3,
    Summing4,
    Summing5,
    Summing6,
    Summing7,
    Summing8,
    Summing9,
    Summing10,
    Summing11,
    Summing12,
    Summing13,
    Summing14,
    Summing15,
    Summing16,
    Summing17,
    Summing18,
    Summing19,
    Summing20,
    Summing21,
    Summing22,
    Summing23,
    Summing24,
    Summing25,
    Summing26,
    Summing27,
    Summing28,
    Summing29,
    Summing30,
    WaitSumming2,
    WordInstr,
    WaitWord1,
    Word1,
    WaitWord2,
    Word2,
    WaitWord3,
    Word3,
    WaitWord4,
    MatInstr,
    WaitMat2,
    Mat1,
    Mat2,
    Mat3,
    Mat4,
    Mat5,
    Mat6,
    Mat7,
    Mat8,
    Mat9,
    Mat10,
    WaitMat,
    FigInstr,
    WaitFig,
    Fig1,
    Fig2,
    Fig3,
    Fig4,
    Fig5,
    Fig6,
    Fig7,
    Fig8,
    Fig9,
    Fig10,
    WaitFig2,
    EQInstr,
    WaitEQ2,
    EQ,
    WaitEQ,
    KnowGInstr,
    WaitKnowG3,
    KnowG1,
    KnowG2,
    KnowG3,
    KnowG4,
    KnowG5,
    KnowG6,
    KnowG7,
    KnowG8,
    KnowG9,
    KnowG10,
    KnowG11,
    KnowG12,
    KnowG13,
    KnowG14,
    KnowG15,
    KnowG16,
    KnowG17,
    KnowG18,
    KnowG19,
    KnowG20,
    KnowG21,
    KnowG22,
    KnowG23,
    KnowG24,
    KnowG25,
    KnowG26,
    KnowG27,
    KnowG28,
    KnowG29,
    KnowG30,
    WaitKnowG2,
    Sur1,
    WaitSur1,
    Sur2,
    WaitSur2,
    Sur3,
    WaitSur3,
    Sur4,
    WaitSur4,
    Sur5,
    WaitSur5,
    Sur6,
    Outro
 ]
