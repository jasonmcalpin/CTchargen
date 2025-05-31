"""
Hyphenation, using Frank Liang's algorithm.

This module provides a single function to hyphenate words. hyphenate_word takes
a string (the word), and returns a list of parts that can be separated by hyphens.

>>> hyphenate_word("hyphenation")
['hy', 'phen', 'ation']
>>> hyphenate_word("supercalifragilisticexpialidocious")
['su', 'per', 'cal', 'ifrag', 'ilis', 'tic', 'ex', 'pi', 'ali', 'do', 'cious']
>>> hyphenate_word("project")
['project']

Ned Batchelder, July 2007.
This Python code is in the public domain.

v1.1 - Updated for CTchargen refactoring
"""

import re
from typing import List, Dict, Any, Optional, Union

__version__ = '1.1.20250530'


class Hyphenator:
    """
    Class for hyphenating words using Frank Liang's algorithm.
    """
    def __init__(self, patterns: str, exceptions: str = ''):
        """
        Initialize the hyphenator with patterns and exceptions.
        
        Args:
            patterns: String containing hyphenation patterns
            exceptions: String containing exception words with hyphens
        """
        self.tree = {}
        for pattern in patterns.split():
            self._insert_pattern(pattern)

        self.exceptions = {}
        for ex in exceptions.split():
            # Convert the hyphenated pattern into a point array for use later.
            self.exceptions[ex.replace('-', '')] = [0] + [int(h == '-') for h in re.split(r"[a-z]", ex)]

    def _insert_pattern(self, pattern: str) -> None:
        """
        Insert a pattern into the pattern tree.
        
        Args:
            pattern: Hyphenation pattern to insert
        """
        # Convert the a pattern like 'a1bc3d4' into a string of chars 'abcd'
        # and a list of points [ 0, 1, 0, 3, 4 ].
        chars = re.sub('[0-9]', '', pattern)
        points = [int(d or 0) for d in re.split("[.a-z]", pattern)]

        # Insert the pattern into the tree. Each character finds a dict
        # another level down in the tree, and leaf nodes have the list of
        # points.
        t = self.tree
        for c in chars:
            if c not in t:
                t[c] = {}
            t = t[c]
        t[None] = points

    def hyphenate_word(self, word: str) -> List[str]:
        """
        Given a word, returns a list of pieces, broken at the possible
        hyphenation points.
        
        Args:
            word: Word to hyphenate
            
        Returns:
            List[str]: List of word parts that can be separated by hyphens
        """
        # Short words aren't hyphenated.
        if len(word) <= 4:
            return [word]
            
        # If the word is an exception, get the stored points.
        if word.lower() in self.exceptions:
            points = self.exceptions[word.lower()]
        else:
            work = '.' + word.lower() + '.'
            points = [0] * (len(work) + 1)
            for i in range(len(work)):
                t = self.tree
                for c in work[i:]:
                    if c in t:
                        t = t[c]
                        if None in t:
                            p = t[None]
                            for j in range(len(p)):
                                points[i + j] = max(points[i + j], p[j])
                    else:
                        break
            # No hyphens in the first two chars or the last two.
            points[1] = points[2] = points[-2] = points[-3] = 0

        # Examine the points to build the pieces list.
        pieces = ['']
        for c, p in zip(word, points[2:]):
            pieces[-1] += c
            if p % 2:
                pieces.append('')
        return pieces


# Load the patterns and exceptions
patterns = (
# Knuth and Liang's original hyphenation patterns from classic TeX.
# In the public domain.
"""
.ach4 .ad4der .af1t .al3t .am5at .an5c .ang4 .ani5m .ant4 .an3te .anti5s .ar5s
.ar4tie .ar4ty .as3c .as1p .as1s .aster5 .atom5 .au1d .av4i .awn4 .ba4g .ba5na
.bas4e .ber4 .be5ra .be3sm .be5sto .bri2 .but4ti .cam4pe .can5c .capa5b .car5ol
.ca4t .ce4la .ch4 .chill5i .ci2 .cit5r .co3e .co4r .cor5ner .de4moi .de3o .de3ra
.de3ri .des4c .dictio5 .do4t .du4c .dumb5 .earth5 .eas3i .eb4 .eer4 .eg2 .el5d
.el3em .enam3 .en3g .en3s .eq5ui5t .er4ri .es3 .eu3 .eye5 .fes3 .for5mer .ga2
.ge2 .gen3t4 .ge5og .gi5a .gi4b .go4r .hand5i .han5k .he2 .hero5i .hes3 .het3
.hi3b .hi3er .hon5ey .hon3o .hov5 .id4l .idol3 .im3m .im5pin .in1 .in3ci .ine2
.in2k .in3s .ir5r .is4i .ju3r .la4cy .la4m .lat5er .lath5 .le2 .leg5e .len4
.lep5 .lev1 .li4g .lig5a .li2n .li3o .li4t .mag5a5 .mal5o .man5a .mar5ti .me2
.mer3c .me5ter .mis1 .mist5i .mon3e .mo3ro .mu5ta .muta5b .ni4c .od2 .odd5
.of5te .or5ato .or3c .or1d .or3t .os3 .os4tl .oth3 .out3 .ped5al .pe5te .pe5tit
.pi4e .pio5n .pi2t .pre3m .ra4c .ran4t .ratio5na .ree2 .re5mit .res2 .re5stat
.ri4g .rit5u .ro4q .ros5t .row5d .ru4d .sci3e .self5 .sell5 .se2n .se5rie .sh2
.si2 .sing4 .st4 .sta5bl .sy2 .ta4 .te4 .ten5an .th2 .ti2 .til4 .tim5o5 .ting4
.tin5k .ton4a .to4p .top5i .tou5s .trib5ut .un1a .un3ce .under5 .un1e .un5k
.un5o .un3u .up3 .ure3 .us5a .ven4de .ve5ra .wil5i .ye4 4ab. a5bal a5ban abe2
ab5erd abi5a ab5it5ab ab5lat ab5o5liz 4abr ab5rog ab3ul a4car ac5ard ac5aro
a5ceou ac1er a5chet 4a2ci a3cie ac1in a3cio ac5rob act5if ac3ul ac4um a2d ad4din
ad5er. 2adi a3dia ad3ica adi4er a3dio a3dit a5diu ad4le ad3ow ad5ran ad4su 4adu
a3duc ad5um ae4r aeri4e a2f aff4 a4gab aga4n ag5ell age4o 4ageu ag1i 4ag4l ag1n
a2go 3agog ag3oni a5guer ag5ul a4gy a3ha a3he ah4l a3ho ai2 a5ia a3ic. ai5ly
a4i4n ain5in ain5o ait5en a1j ak1en al5ab al3ad a4lar 4aldi 2ale al3end a4lenti
a5le5o al1i al4ia. ali4e al5lev 4allic 4alm a5log. a4ly. 4alys 5a5lyst 5alyt
3alyz 4ama am5ab am3ag ama5ra am5asc a4matis a4m5ato am5era am3ic am5if am5ily
am1in ami4no a2mo a5mon amor5i amp5en a2n an3age 3analy a3nar an3arc anar4i
a3nati 4and ande4s an3dis an1dl an4dow a5nee a3nen an5est. a3neu 2ang ang5ie
an1gl a4n1ic a3nies an3i3f an4ime a5nimi a5nine an3io a3nip an3ish an3it a3niu
an4kli 5anniz ano4 an5ot anoth5 an2sa an4sco an4sn an2sp ans3po an4st an4sur
antal4 an4tie 4anto an2tr an4tw an3ua an3ul a5nur 4ao apar4 ap5at ap5ero a3pher
4aphi a4pilla ap5illar ap3in ap3ita a3pitu a2pl apoc5 ap5ola apor5i apos3t
aps5es a3pu aque5 2a2r ar3act a5rade ar5adis ar3al a5ramete aran4g ara3p ar4at
4tarc 4tare ta3riz tas4e ta5sy 4tatic ta4tur taun4 tav4 2taw tax4is 2t1b
4tc t4ch tch5et 4t1d 4te. tead4i 4teat tece4 5tect 2t1ed te5di 1tee teg4 te5ger
te5gi 3tel. teli4 5tels te2ma2 tem3at 3tenan 3tenc 3tend 4tenes 1tent ten4tag
1teo te4p te5pe ter3c 5ter3d 1teri ter5ies ter3is teri5za 5ternit ter5v 4tes.
4tess t3ess. teth5e 3teu 3tex 4tey 2t1f 4t1g 2th. than4 th2e 4thea th3eas the5at
the3is 3thet th5ic. th5ica 4thil 5think 4thl th5ode 5thodic 4thoo thor5it
tho5riz 2ths 1tia ti4ab ti4ato 2ti2b 4tick t4ico t4ic1u 5tidi 3tien tif2 ti5fy
2tig 5tigu till5in 1tim 4timp tim5ul 2t1in t2ina 3tine. 3tini 1tio ti5oc tion5ee
5tiq ti3sa 3tise tis4m ti5so tis4p 5tistica ti3tl ti4u 1tiv tiv4a 1tiz ti3za
ti3zen 2tl t5la tlan4 3tle. 3tled 3tles. t5let. t5lo 4t1m tme4 2t1n2 1to to3b
to5crat 4todo 2tof to2gr to5ic to2ma tom4b to3my ton4ali to3nat 4tono 4tony
to2ra to3rie tor5iz tos2 5tour 4tout to3war 4t1p 1tra tra3b tra5ch traci4
trac4it trac4te tras4 tra5ven trav5es5 tre5f tre4m trem5i 5tria tri5ces 5tricia
4trics 2trim tri4v tro5mi tron5i 4trony tro5phe tro3sp tro3v tru5i trus4 4t1s2
t4sc tsh4 t4sw 4t3t2 t4tes t5to ttu4 1tu tu1a tu3ar tu4bi tud2 4tue 4tuf4 5tu3i
3tum tu4nis 2t3up. 3ture 5turi tur3is tur5o tu5ry 3tus 4tv tw4 4t1wa twis4 4two
1ty 4tya 2tyl type3 ty5ph 4tz tz4e 4uab uac4 ua5na uan4i uar5ant uar2d uar3i
uar3t u1at uav4 ub4e u4bel u3ber u4bero u1b4i u4b5ing u3ble. u3ca uci4b uc4it
ucle3 u3cr u3cu u4cy ud5d ud3er ud5est udev4 u1dic ud3ied ud3ies ud5is u5dit
u4don ud4si u4du u4ene uens4 uen4te uer4il 3ufa u3fl ugh3en ug5in 2ui2 uil5iz
ui4n u1ing uir4m uita4 uiv3 uiv4er. u5j 4uk u1la ula5b u5lati ulch4 5ulche
ul3der ul4e u1len ul4gi ul2i u5lia ul3ing ul5ish ul4lar ul4li4b ul4lis 4ul3m
u1l4o 4uls uls5es ul1ti ultra3 4ultu u3lu ul5ul ul5v um5ab um4bi um4bly u1mi
u4m3ing umor5o um2p unat4 u2ne un4er u1ni un4im u2nin un5ish uni3v un3s4 un4sw
unt3ab un4ter. un4tes unu4 un5y un5z u4ors u5os u1ou u1pe uper5s u5pia up3ing
u3pl up3p upport5 upt5ib uptu4 u1ra 4ura. u4rag u4ras ur4be urc4 ur1d ure5at
ur4fer ur4fr u3rif uri4fic ur1in u3rio u1rit ur3iz ur2l url5ing. ur4no uros4
ur4pe ur4pi urs5er ur5tes ur3the urti4 ur4tie u3ru 2us u5sad u5san us4ap usc2
us3ci use5a u5sia u3sic us4lin us1p us5sl us5tere us1tr u2su usur4 uta4b u3tat
4ute. 4utel 4uten uten4i 4u1t2i uti5liz u3tine ut3ing ution5a u4tis 5u5tiz u4t1l
ut5of uto5g uto5matic u5ton u4tou uts4 u3u uu4m u1v2 uxu3 uz4e 1va 5va. 2v1a4b
vac5il vac3u vag4 va4ge va5lie val5o val1u va5mo va5niz va5pi var5ied 3vat 4ve.
4ved veg3 v3el. vel3li ve4lo v4ely ven3om v5enue v4erd 5vere. v4erel v3eren
ver5enc v4eres ver3ie vermi4n 3verse ver3th v4e2s 4ves. ves4te ve4te vet3er
ve4ty vi5ali 5vian 5vide. 5vided 4v3iden 5vides 5vidi v3if vi5gn vik4 2vil
5vilit v3i3liz v1in 4vi4na v2inc vin5d 4ving vio3l v3io4r vi1ou vi4p vi5ro
vis3it vi3so vi3su 4viti vit3r 4vity 3viv 5vo. voi4 3vok vo4la v5ole 5volt 3volv
vom5i vor5ab vori4 vo4ry vo4ta 4votee 4vv4 v4y w5abl 2wac wa5ger wag5o wait5
w5al. wam4 war4t was4t wa1te wa5ver w1b wea5rie weath3 wed4n weet3 wee5v wel4l
w1er west3 w3ev whi4 wi2 wil2 will5in win4de win4g wir4 3wise with3 wiz5 w4k
wl4es wl3in w4no 1wo2 wom1 wo5ven w5p wra4 wri4 writa4 w3sh ws4l ws4pe w5s4t 4wt
wy4 x1a xac5e x4ago xam3 x4ap xas5 x3c2 x1e xe4cuto x2ed xer4i xe5ro x1h xhi2
xhil5 xhu4 x3i xi5a xi5c xi5di x4ime xi5miz x3o x4ob x3p xpan4d xpecto5 xpe3d
x1t2 x3ti x1u xu3a xx4 y5ac 3yar4 y5at y1b y1c y2ce yc5er y3ch ych4e ycom4 ycot4
y1d y5ee y1er y4erf yes4 ye4t y5gi 4y3h y1i y3la ylla5bl y3lo y5lu ymbol5 yme4
ympa3 yn3chr yn5d yn5g yn5ic 5ynx y1o4 yo5d y4o5g yom4 yo5net y4ons y4os y4ped
yper5 yp3i y3po y4poc yp2ta y5pu yra5m yr5ia y3ro yr4r ys4c y3s2e ys3ica ys3io
3ysis y4so yss4 ys1t ys3ta ysur4 y3thin yt3ic y1w za1 z5a2b zar2 4zb 2ze ze4n
ze4p z1er ze3ro zet4 2z1i z4il z4is 5zl 4zm 1zo zo4m zo5ol zte4 4z1z2 z4zy
"""
# Extra patterns, from ushyphmax.tex, dated 2005-05-30.
# Copyright (C) 1990, 2004, 2005 Gerard D.C. Kuiken.
# Copying and distribution of this file, with or without modification,
# are permitted in any medium without royalty provided the copyright
# notice and this notice are preserved.
#
# These patterns are based on the Hyphenation Exception Log
# published in TUGboat, Volume 10 (1989), No. 3, pp. 337-341,
# and a large number of incorrectly hyphenated words not yet published.
"""
.con5gr .de5riva .dri5v4 .eth1y6l1 .eu4ler .ev2 .ever5si5b .ga4s1om1 .ge4ome
.ge5ot1 .he3mo1 .he3p6a .he3roe .in5u2t .kil2n3i .ko6r1te1 .le6ices .me4ga1l
.met4ala .mim5i2c1 .mi1s4ers .ne6o3f .noe1th .non1e2m .poly1s .post1am .pre1am
.rav5en1o .semi5 .sem4ic .semid6 .semip4 .semir4 .sem6is4 .semiv4 .sph6in1
.spin1o .ta5pes1tr .te3legr .to6pog .to2q .un3at5t .un5err5 .vi2c3ar .we2b1l
.re1e4c a5bolic a2cabl af6fish am1en3ta5b anal6ys ano5a2c ans5gr ans3v anti1d
an3ti1n2 anti1re a4pe5able ar3che5t ar2range as5ymptot ath3er1o1s at6tes.
augh4tl au5li5f av3iou back2er. ba6r1onie ba1thy bbi4t be2vie bi5d2if bil2lab
bio5m bi1orb bio1rh b1i3tive blan2d1 blin2d1 blon2d2 bor1no5 bo2t1u1l brus4q
bus6i2er bus6i2es buss4ing but2ed. but4ted cad5e1m cat1a1s2 4chs. chs3hu chie5vo
cig3a3r cin2q cle4ar co6ph1o3n cous2ti cri3tie croc1o1d cro5e2co c2tro3me6c
1cu2r1ance 2d3alone data1b dd5a5b d2d5ib de4als. de5clar1 de2c5lina de3fin3iti
de2mos des3ic de2tic dic1aid dif5fra 3di1methy di2ren di2rer 2d1lead 2d1li2e
3do5word dren1a5l drif2t1a d1ri3pleg5 drom3e5d d3tab du2al. du1op1o1l ea4n3ies
e3chas edg1l ed1uling eli2t1is e1loa en1dix eo3grap 1e6p3i3neph1 e2r3i4an.
e3spac6i eth1y6l1ene 5eu2clid1 feb1rua fermi1o 3fich fit5ted. fla1g6el flow2er.
3fluor gen2cy. ge3o1d ght1we g1lead get2ic. 4g1lish 5glo5bin 1g2nac gnet1ism
gno5mo g2n1or. g2noresp 2g1o4n3i1za graph5er. griev1 g1utan hair1s ha2p3ar5r
hatch1 hex2a3 hite3sid h3i5pel1a4 hnau3z ho6r1ic. h2t1eou hypo1tha id4ios
ifac1et ign4it ignit1er i4jk im3ped3a infra1s2 i5nitely. irre6v3oc i1tesima
ith5i2l itin5er5ar janu3a japan1e2s je1re1m 1ke6ling 1ki5netic 1kovian k3sha
la4c3i5e lai6n3ess lar5ce1n l3chai l3chil6d1 lead6er. lea4s1a 1lec3ta6b
le3g6en2dre 1le1noid lith1o5g ll1fl l2l3ish l5mo3nell lo1bot1o1 lo2ges. load4ed.
load6er. l3tea lth5i2ly lue1p 1lunk3er 1lum5bia. 3lyg1a1mi ly5styr ma1la1p m2an.
man3u1sc mar1gin1 medi2c med3i3cin medio6c1 me3gran3 m2en. 3mi3da5b 3milita
mil2l1ag mil5li5li mi6n3is. mi1n2ut1er mi1n2ut1est m3ma1b 5maph1ro1 5moc1ra1t
mo5e2las mol1e5c mon4ey1l mono3ch mo4no1en moro6n5is mono1s6 moth4et2 m1ou3sin
m5shack2 mu2dro mul2ti5u n3ar4chs. n3ch2es1t ne3back 2ne1ski n1dieck nd3thr
nfi6n3ites 4n5i4an. nge5nes ng1ho ng1spr nk3rup n5less 5noc3er1os nom1a6l
nom5e1no n1o1mist non1eq non1i4so 5nop1oly. no1vemb ns5ceiv ns4moo ntre1p
obli2g1 o3chas odel3li odit1ic oerst2 oke1st o3les3ter oli3gop1o1 o1lo3n4om
o3mecha6 onom1ic o3norma o3no2t1o3n o3nou op1ism. or4tho3ni4t orth1ri or5tively
o4s3pher o5test1er o5tes3tor oth3e1o1s ou3ba3do o6v3i4an. oxi6d1ic pal6mat
parag6ra4 par4a1le param4 para3me pee2v1 phi2l3ant phi5lat1e3l pi2c1a3d pli2c1ab
pli5nar poin3ca 1pole. poly1e po3lyph1ono 1prema3c pre1neu pres2pli pro2cess
proc3i3ty. pro2g1e 3pseu2d pseu3d6o3d2 pseu3d6o3f2 pto3mat4 p5trol3 pu5bes5c
quain2t1e qu6a3si3 quasir6 quasis6 quin5tes5s qui3v4ar r1abolic 3rab1o1loi
ra3chu r3a3dig radi1o6g r2amen 3ra4m5e1triz ra3mou ra5n2has ra1or r3bin1ge
re2c3i1pr rec5t6ang re4t1ribu r3ial. riv1o1l 6rk. rk1ho r1krau 6rks. r5le5qu
ro1bot1 ro5e2las ro5epide1 ro3mesh ro1tron r3pau5li rse1rad1i r1thou r1treu
r1veil rz1sc sales3c sales5w 5sa3par5il sca6p1er sca2t1ol s4chitz schro1ding1
1sci2utt scrap4er. scy4th1 sem1a1ph se3mes1t se1mi6t5ic sep3temb shoe1st sid2ed.
side5st side5sw si5resid sky1sc 3slova1kia 3s2og1a1my so2lute 3s2pace 1s2pacin
spe3cio spher1o spi2c1il spokes5w sports3c sports3w s3qui3to s2s1a3chu1 ss3hat
s2s3i4an. s5sign5a3b 1s2tamp s2t1ant5shi star3tli sta1ti st5b 1stor1ab strat1a1g
strib5ut st5scr stu1pi4d1 styl1is su2per1e6 1sync 1syth3i2 swimm6 5tab1o1lism
ta3gon. talk1a5 t1a1min t6ap6ath 5tar2rh tch1c tch3i1er t1cr teach4er. tele2g
tele1r6o 3ter1gei ter2ic. t3ess2es tha4l1am tho3don th1o5gen1i tho1k2er thy4l1an
thy3sc 2t3i4an. ti2n3o1m t1li2er tolo2gy tot3ic trai3tor1 tra1vers travers3a3b
treach1e tr4ial. 3tro1le1um trof4ic. tro3fit tro1p2is 3trop1o5les 3trop1o5lis
t1ro1pol3it tsch3ie ttrib1ut1 turn3ar t1wh ty2p5al ua3drati uad1ratu u5do3ny
uea1m u2r1al. uri4al. us2er. v1ativ v1oir5du1 va6guer vaude3v 1verely. v1er1eig
ves1tite vi1vip3a3r voice1p waste3w6a2 wave1g4 w3c week1n wide5sp wo4k1en
wrap3aro writ6er. x1q xquis3 y5che3d ym5e5try y1stro yes5ter1y z3ian. z3o1phr
z2z3w
""")

exceptions = """
as-so-ciate as-so-ciates dec-li-na-tion oblig-a-tory phil-an-thropic present
presents project projects reci-procity re-cog-ni-zance ref-or-ma-tion
ret-ri-bu-tion ta-ble
"""

# Create a singleton instance
hyphenator = Hyphenator(patterns, exceptions)
hyphenate_word = hyphenator.hyphenate_word

# Clean up namespace
del patterns
del exceptions


if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        for word in sys.argv[1:]:
            print('-'.join(hyphenate_word(word)))
    else:
        import doctest
        doctest.testmod(verbose=True)
