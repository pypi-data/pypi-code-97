#!/usr/bin/env python

#******************************************************************************
#
#  rpnCalendar.py
#
#  rpnChilada calendar operators
#  copyright (c) 2021, Rick Gutleber (rickg@his.com)
#
#  License: GNU GPL 3.0 (see <http://www.gnu.org/licenses/gpl.html> for more
#  information).
#
#******************************************************************************

import calendar

from convertdate import bahai, french_republican, hebrew, indian_civil, islamic, julian, \
                        julianday, mayan, persian
from ethiopian_date import EthiopianDateConverter as ethiopian_date
from mpmath import ceil

from rpn.rpnDateTime import RPNDateTime
from rpn.rpnName import getOrdinalName
from rpn.rpnUtils import oneArgFunctionEvaluator
from rpn.rpnValidator import argValidator, DateTimeValidator, IntValidator, YearValidator

#******************************************************************************
#
#  calendar names
#
#******************************************************************************

bahaiYears = [
    'Alif',
    'Ba\'',
    'Ab',
    'Dal',
    'Bab',
    'Vav',
    'Abad',
    'Jad',
    'Baha\'',
    'Hubb',
    'Bahhaj',
    'Javab',
    'Ahad',
    'Vahhab',
    'Vidad',
    'Badi`',
    'Bahi',
    'Abha',
    'Vahid',
]

bahaiMonths = [
    'Baha',
    'Jalal',
    'Jamal',
    '`Azamat',
    'Nur',
    'Rahmat',
    'Kalimat',
    'Kamal',
    'Asma\'',
    '`Izzat',
    'Mashiyyat',
    '`Ilm',
    'Qudrat',
    'Qawl',
    'Masa\'il',
    'Sharaf',
    'Sultan',
    'Mulk',
    'Ayyam-i-Ha',
    '`Ala\''
]

bahaiDays = [
    'Kamal',     # Monday
    'Fidal',
    '`Idal',
    'Istijlal',
    'Istiqlal',
    'Jalal',
    'Jamal'
]

hebrewMonths = [
    'Nisan',
    'Iyar',
    'Sivan',
    'Tammuz',
    'Av',
    'Elul',
    'Tishrei',
    'Marcheshvan',
    'Kislev',
    'Tevet',
    'Shevat',
    'Adar I',
    'Adar II'
]

hebrewDays = [
    'Yom Sheni',     # Monday
    'Yom Shlishi',
    'Yom Revi\'i',
    'Yom Chamishi',
    'Yom Shishi',
    'Yom Shabbat',
    'Yom Rishon'
]

indianCivilDays = [
    'Somavara',     # Monday
    'Mangalavara',
    'Budhavara',
    'Guruvara',
    'Sukravara',
    'Sanivara',
    'Ravivara',
]

indianCivilMonths = [
    'Chaitra',
    'Vaishakha',
    'Jyeshtha',
    'Ashadha',
    'Shravana',
    'Bhaadra',
    'Ashwin',
    'Kartika',
    'Agrahayana',
    'Pausha',
    'Magha',
    'Phalguna',
]

islamicMonths = [
    'Muharram',
    'Safar',
    'Rabi al-Awwal',
    'Rabi ath-Thani',
    'Jumada al-Ula',
    'Jumada ath-Thaniyah',
    'Rajab',
    'Sha`ban',
    'Ramadan',
    'Shawwal',
    'Dhu al-Qa`dah',
    'Dhu al-Hijjah'
]

islamicDays = [
    'al-Ithnayn',   # Monday
    'ath-Thulatha',
    'al-Arbi`a',
    'al-Khamis',
    'al-Jumu`ah',
    'as-Sabt',
    'al-Ahad'
]

persianMonths = [
    'Farvardin',
    'Ordibehesht',
    'Khordad',
    'Tir',
    'Mordad',
    'Shahrivar',
    'Mehr',
    'Aban',
    'Azar',
    'Dey',
    'Bahman',
    'Esfand'
]

persianDays = [
    'Yekshanbeh',   # Monday
    'Doshanbeh',
    'Seshhanbeh',
    'Chaharshanbeh',
    'Panjshanbeh',
    'Jomeh',
    'Shanbeh'
]

ethiopianMonths = [
    'Meskerem',
    'Thikimt',
    'Hidar',
    'Tahsas',
    'Thir',
    'Yekatit',
    'Megabit',
    'Miyazya',
    'Ginbot',
    'Senie',
    'Hamlie',
    'Nehasie',
    'Phagumien'
]

ethiopianDays = [
    'Lideta',
    'Aba Guba',
    'Be\'Eta',
    'Yohannes',
    'Abo',
    'Iyesus',
    'Selassie',
    'Aba Kiros',
    'Tomas',
    'Meskel',
    'Hana Mariam',
    'Michael',
    'Egziher Ab',
    'Abune Aregawi',
    'K\'irk\'os',
    'Kidane Mihret',
    'Est\'ifanos',
    'Tekle Alfa',
    'Gabriel',
    'Hintsite',
    'Mariam',
    'Ura\'el',
    'Giorgis',
    'Tekle Haimanot',
    'Merk\'orios',
    'Yosef',
    'Medhani Alem',
    'Amanu\'el',
    'Bale Egziabeir',
    'Mark\'os'
]

frenchRepublicanDays = [
    'Primidi',
    'Duodi',
    'Tridi',
    'Quartidi',
    'Quintidi',
    'Sextidi',
    'Septidi',
    'Octidi',
    'Nonidi',
    'Decadi'
]

frenchRepublicanMonths = [
    'Vendemiaire',
    'Brumaire',
    'Frimaire',
    'Nivose',
    'Pluviose',
    'Ventose',
    'Germinal',
    'Floreal',
    'Prairial',
    'Messidor',
    'Thermidor',
    'Fructidor',
    'Sansculottides'
]


#******************************************************************************
#
#  getOrdinalDateOperator
#
#******************************************************************************

@oneArgFunctionEvaluator( )
@argValidator( [ DateTimeValidator( ) ] )
def getOrdinalDateOperator( n ):
    return str( n.year ) + '-' + str( n.timetuple( ).tm_yday )


#******************************************************************************
#
#  generateMonthCalendarOperator
#
#******************************************************************************

@oneArgFunctionEvaluator( )
@argValidator( [ DateTimeValidator( ) ] )
def generateMonthCalendarOperator( datetime ):
    cal = calendar.TextCalendar( firstweekday = 6 )
    print( )
    cal.prmonth( datetime.year, datetime.month )
    print( )

    return [ datetime.year, datetime.month ]


#******************************************************************************
#
#  generateYearCalendarOperator
#
#******************************************************************************

@oneArgFunctionEvaluator( )
@argValidator( [ YearValidator( ) ] )
def generateYearCalendarOperator( n ):
    cal = calendar.TextCalendar( firstweekday = 6 )

    if isinstance( n, RPNDateTime ):
        cal.pryear( n.year )
    else:
        cal.pryear( int( n ) )

    return ''


#******************************************************************************
#
#  getJulianDayOperator
#
#******************************************************************************

@oneArgFunctionEvaluator( )
@argValidator( [ DateTimeValidator( ) ] )
def getJulianDayOperator( n ):
    n.to( 'utc' )
    return julianday.from_datetime( n )


#******************************************************************************
#
#  getLilianDayOperator
#
#******************************************************************************

@oneArgFunctionEvaluator( )
@argValidator( [ DateTimeValidator( ) ] )
def getLilianDayOperator( n ):
    return ceil( n.subtract( RPNDateTime( 1582, 10, 15 ) ).value )


#******************************************************************************
#
#  getISODateOperator
#
#******************************************************************************

@oneArgFunctionEvaluator( )
@argValidator( [ DateTimeValidator( ) ] )
def getISODateOperator( n ):
    result = n.isocalendar( )

    return list( result )


#******************************************************************************
#
#  getISODateNameOperator
#
#******************************************************************************

@oneArgFunctionEvaluator( )
@argValidator( [ DateTimeValidator( ) ] )
def getISODateNameOperator( n ):
    result = n.isocalendar( )

    return str( result[ 0 ] ) + '-W' + str( result[ 1 ] ) + '-' + str( result[ 2 ] )


#******************************************************************************
#
#  getHebrewCalendarDateOperator
#
#******************************************************************************

@oneArgFunctionEvaluator( )
@argValidator( [ DateTimeValidator( ) ] )
def getHebrewCalendarDateOperator( n ):
    return list( hebrew.from_gregorian( n.year, n.month, n.day ) )


#******************************************************************************
#
#  convertHebrewDateOperator
#
#******************************************************************************

@argValidator( [ IntValidator( 1 ), IntValidator( 1, 13 ), IntValidator( 1, 30 ) ] )
def convertHebrewDateOperator( year, month, day ):
    return RPNDateTime( *hebrew.to_gregorian( int( year ), int( month ), int( day ) ), dateOnly = True )


#******************************************************************************
#
#  getHebrewCalendarDateNameOperator
#
#******************************************************************************

@oneArgFunctionEvaluator( )
@argValidator( [ DateTimeValidator( ) ] )
def getHebrewCalendarDateNameOperator( n ):
    date = hebrew.from_gregorian( n.year, n.month, n.day )

    return hebrewDays[ n.weekday( ) ] + ', ' + hebrewMonths[ date[ 1 ] - 1 ] + \
           ' ' + str( date[ 2 ] ) + ', ' + str( date[ 0 ] )


#******************************************************************************
#
#  getIndianCivilCalendarDateOperator
#
#******************************************************************************

@oneArgFunctionEvaluator( )
@argValidator( [ DateTimeValidator( ) ] )
def getIndianCivilCalendarDateOperator( n ):
    return list( indian_civil.from_gregorian( n.year, n.month, n.day ) )


#******************************************************************************
#
#  convertIndianCivilDateOperator
#
#******************************************************************************

@argValidator( [ IntValidator( 1 ), IntValidator( 1, 12 ), IntValidator( 1, 31 ) ] )
def convertIndianCivilDateOperator( year, month, day ):
    return RPNDateTime( *indian_civil.to_gregorian( int( year ), int( month ), int( day ) ), dateOnly = True )


#******************************************************************************
#
#  getIndianCivilCalendarDateNameOperator
#
#******************************************************************************

@oneArgFunctionEvaluator( )
@argValidator( [ DateTimeValidator( ) ] )
def getIndianCivilCalendarDateNameOperator( n ):
    date = indian_civil.from_gregorian( n.year, n.month, n.day )

    return indianCivilDays[ n.weekday( ) ] + ', ' + indianCivilMonths[ date[ 1 ] - 1 ] + \
           ' ' + str( date[ 2 ] ) + ', ' + str( date[ 0 ] )


#******************************************************************************
#
#  getMayanCalendarDateOperator
#
#******************************************************************************

@oneArgFunctionEvaluator( )
@argValidator( [ DateTimeValidator( ) ] )
def getMayanCalendarDateOperator( n ):
    return list( mayan.from_gregorian( n.year, n.month, n.day ) )


#******************************************************************************
#
#  convertMayanDateOperator
#
#******************************************************************************

@argValidator( [ IntValidator( ), IntValidator( 0 ), IntValidator( 0 ), IntValidator( 0 ), IntValidator( 0 ) ] )
def convertMayanDateOperator( baktun, katun, tun, uinal, kin ):
    return RPNDateTime( *mayan.to_gregorian( baktun, katun, tun, uinal, kin ), dateOnly = True )


#******************************************************************************
#
#  getIslamicCalendarDateOperator
#
#******************************************************************************

@oneArgFunctionEvaluator( )
@argValidator( [ DateTimeValidator( ) ] )
def getIslamicCalendarDateOperator( n ):
    return list( islamic.from_gregorian( n.year, n.month, n.day ) )


#******************************************************************************
#
#  convertIslamicDateOperator
#
#******************************************************************************

@argValidator( [ IntValidator( 1 ), IntValidator( 1, 12 ), IntValidator( 1, 31 ) ] )
def convertIslamicDateOperator( year, month, day ):
    return RPNDateTime( *islamic.to_gregorian( int( year ), int( month ), int( day ) ), dateOnly = True )


#******************************************************************************
#
#  getIslamicCalendarDateNameOperator
#
#******************************************************************************

@oneArgFunctionEvaluator( )
@argValidator( [ DateTimeValidator( ) ] )
def getIslamicCalendarDateNameOperator( n ):
    date = islamic.from_gregorian( n.year, n.month, n.day )

    return islamicDays[ n.weekday( ) ] + ', ' + islamicMonths[ date[ 1 ] - 1 ] + \
           ' ' + str( date[ 2 ] ) + ', ' + str( date[ 0 ] )


#******************************************************************************
#
#  getJulianCalendarDateOperator
#
#******************************************************************************

@oneArgFunctionEvaluator( )
@argValidator( [ DateTimeValidator( ) ] )
def getJulianCalendarDateOperator( n ):
    return list( julian.from_gregorian( n.year, n.month, n.day ) )


#******************************************************************************
#
#  convertJulianDateOperator
#
#******************************************************************************

@argValidator( [ IntValidator( ), IntValidator( 1, 12 ), IntValidator( 1, 31 ) ] )
def convertJulianDateOperator( year, month, day ):
    return RPNDateTime( *julian.to_gregorian( int( year ), int( month ), int( day ) ), dateOnly = True )


#******************************************************************************
#
#  getPersianCalendarDateOperator
#
#******************************************************************************

@oneArgFunctionEvaluator( )
@argValidator( [ DateTimeValidator( ) ] )
def getPersianCalendarDateOperator( n ):
    return list( persian.from_gregorian( n.year, n.month, n.day ) )


#******************************************************************************
#
#  convertPersianDateOperator
#
#******************************************************************************

@argValidator( [ IntValidator( ), IntValidator( 1, 12 ), IntValidator( 1, 31 ) ] )
def convertPersianDateOperator( year, month, day ):
    return RPNDateTime( *persian.to_gregorian( int( year ), int( month ), int( day ) ), dateOnly = True )


#******************************************************************************
#
#  getPersianCalendarDateNameOperator
#
#******************************************************************************

@oneArgFunctionEvaluator( )
@argValidator( [ DateTimeValidator( ) ] )
def getPersianCalendarDateNameOperator( n ):
    date = persian.from_gregorian( n.year, n.month, n.day )

    return persianDays[ n.weekday( ) ] + ', ' + persianMonths[ date[ 1 ] - 1 ] + \
           ' ' + str( date[ 2 ] ) + ', ' + str( date[ 0 ] )


#******************************************************************************
#
#  getBahaiCalendarDateOperator
#
#******************************************************************************

@oneArgFunctionEvaluator( )
@argValidator( [ DateTimeValidator( ) ] )
def getBahaiCalendarDateOperator( n ):
    return list( bahai.from_gregorian( n.year, n.month, n.day ) )


#******************************************************************************
#
#  convertBahaiDateOperator
#
#******************************************************************************

@argValidator( [ IntValidator( ), IntValidator( 1, 19 ), IntValidator( 1, 31 ) ] )
def convertBahaiDateOperator( year, month, day ):
    return RPNDateTime( *bahai.to_gregorian( int( year ), int( month ), int( day ) ), dateOnly = True )


#******************************************************************************
#
#  getBahaiCalendarDateNameOperator
#
#******************************************************************************

@oneArgFunctionEvaluator( )
@argValidator( [ DateTimeValidator( ) ] )
def getBahaiCalendarDateNameOperator( n ):
    date = bahai.from_gregorian( n.year, n.month, n.day )

    result = bahaiDays[ n.weekday( ) ] + ', ' + bahaiMonths[ date[ 1 ] - 1 ] + \
           ' ' + str( date[ 2 ] ) + ', '

    if date[ 0 ] >= 1:
        result += 'Year ' + bahaiYears[ date[ 0 ] % 19 - 1 ] + ' of the ' + \
                  getOrdinalName( ( date[ 0 ] // 19 ) + 1 ) + ' Vahid of the ' + \
                  getOrdinalName( ( date[ 0 ] // 361 ) + 1 ) + ' Kull-i-Shay\'' + \
                  ' (Year ' + str( date[ 0 ] ) + ')'
    else:
        result += str( date[ 0 ] )

    return result


#******************************************************************************
#
#  getEthiopianCalendarDateOperator
#
#******************************************************************************

@oneArgFunctionEvaluator( )
@argValidator( [ DateTimeValidator( ) ] )
def getEthiopianCalendarDateOperator( n ):
    return list( ethiopian_date.to_ethiopian( n.year, n.month, n.day ) )


#******************************************************************************
#
#  convertEthiopianDateOperator
#
#******************************************************************************

@argValidator( [ IntValidator( ), IntValidator( 1, 12 ), IntValidator( 1, 31 ) ] )
def convertEthiopianDateOperator( year, month, day ):
    ethDate = ethiopian_date.to_gregorian( int( year ), int( month ), int( day ) )
    return RPNDateTime( ethDate.year, ethDate.month, ethDate.day )


#******************************************************************************
#
#  getEthiopianCalendarDateNameOperator
#
#******************************************************************************

@oneArgFunctionEvaluator( )
@argValidator( [ DateTimeValidator( ) ] )
def getEthiopianCalendarDateNameOperator( n ):
    date = list( ethiopian_date.to_ethiopian( n.year, n.month, n.day ) )

    return ethiopianDays[ date[ 2 ] - 1 ] + ' ' + ethiopianMonths[ date[ 1 ] - 1 ] + \
                          ' ' + str( date[ 0 ] )


#******************************************************************************
#
#  getFrenchRepublicanCalendarDateOperator
#
#******************************************************************************

@oneArgFunctionEvaluator( )
@argValidator( [ DateTimeValidator( ) ] )
def getFrenchRepublicanCalendarDateOperator( n ):
    return list( french_republican.from_gregorian( n.year, n.month, n.day ) )


#******************************************************************************
#
#  convertFrenchRepublicanDateOperator
#
#******************************************************************************

@argValidator( [ IntValidator( ), IntValidator( 1, 13 ), IntValidator( 1, 31 ) ] )
def convertFrenchRepublicanDateOperator( year, month, day ):
    return RPNDateTime( *french_republican.to_gregorian( int( year ), int( month ), int( day ) ), dateOnly = True )


#******************************************************************************
#
#  getFrenchRepublicanCalendarDateNameOperator
#
#******************************************************************************

@oneArgFunctionEvaluator( )
@argValidator( [ DateTimeValidator( ) ] )
def getFrenchRepublicanCalendarDateNameOperator( n ):
    date = french_republican.from_gregorian( n.year, n.month, n.day )

    #return frenchRepublicanDays[ n.weekday( ) ] + ', ' + frenchRepublicanMonths[ date[ 1 ] - 1 ] + \
    #       ' ' + str( date[ 2 ] ) + ', ' + str( int( date[ 0 ] ) )
    return frenchRepublicanMonths[ date[ 1 ] - 1 ] + \
           ' ' + str( date[ 2 ] ) + ', ' + str( int( date[ 0 ] ) )
