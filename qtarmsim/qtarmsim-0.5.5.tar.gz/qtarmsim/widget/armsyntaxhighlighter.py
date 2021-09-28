# -*- coding: utf-8 -*-

###########################################################################
#                                                                         #
#  This file is part of QtARMSim.                                         #
#                                                                         #
#  QtARMSim is free software: you can redistribute it and/or modify       #
#  it under the terms of the GNU General Public License as published by   #
#  the Free Software Foundation; either version 3 of the License, or      #
#  (at your option) any later version.                                    #
#                                                                         #
#  This program is distributed in the hope that it will be useful, but    #
#  WITHOUT ANY WARRANTY; without even the implied warranty of             #
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU      #
#  General Public License for more details.                               #
#                                                                         #
###########################################################################

# =========================================================================
#  References:
#   http://doc.qt.io/qt-5/qtwidgets-richtext-syntaxhighlighter-example.html
# =========================================================================

from PySide2 import QtCore, QtGui


def generateHighlightingRules():
    #
    # Most of the following ARM keywords and directives were obtained from the listings ARM definition for LaTeX (c)
    # 2013 by Jacques Supcik
    #
    keywords = """
                adc,adcal,adcals,adccc,adcccs,adccs,adccss,adceq,adceqs,
                adcge,adcges,adcgt,adcgts,adchi,adchis,adchs,adchss,adcle,adcles,
                adclo,adclos,adcls,adclss,adclt,adclts,adcmi,adcmis,adcne,adcnes,
                adcpl,adcpls,adcs,adcvc,adcvcs,adcvs,adcvss,add,addal,addals,addcc,
                addccs,addcs,addcss,addeq,addeqs,addge,addges,addgt,addgts,addhi,
                addhis,addhs,addhss,addle,addles,addlo,addlos,addls,addlss,addlt,
                addlts,addmi,addmis,addne,addnes,addpl,addpls,adds,addvc,addvcs,addvs,
                addvss,and,andal,andals,andcc,andccs,andcs,andcss,andeq,andeqs,andge,
                andges,andgt,andgts,andhi,andhis,andhs,andhss,andle,andles,andlo,
                andlos,andls,andlss,andlt,andlts,andmi,andmis,andne,andnes,andpl,
                andpls,ands,andvc,andvcs,andvs,andvss,asr,asrs,b,bal,bcc,bcs,beq,bge,bgt,bhi,
                bhs,bic,bical,bicals,biccc,bicccs,biccs,biccss,biceq,biceqs,bicge,
                bicges,bicgt,bicgts,bichi,bichis,bichs,bichss,bicle,bicles,biclo,
                biclos,bicls,biclss,biclt,biclts,bicmi,bicmis,bicne,bicnes,bicpl,
                bicpls,bics,bicvc,bicvcs,bicvs,bicvss,bkpt,bl,blal,blcc,blcs,ble,bleq,
                blge,blgt,blhi,blhs,blle,bllo,blls,bllt,blmi,blne,blo,blpl,bls,blt,
                blvc,blvs,blx,blxal,blxcc,blxcs,blxeq,blxge,blxgt,blxhi,blxhs,blxle,
                blxlo,blxls,blxlt,blxmi,blxne,blxpl,blxvc,blxvs,bmi,bne,bpl,bvc,bvs,
                bXX,
                bx,bxal,bxcc,bxcs,bxeq,bxge,bxgt,bxhi,bxhs,bxj,bxjal,bxjcc,bxjcs,
                bxjeq,bxjge,bxjgt,bxjhi,bxjhs,bxjle,bxjlo,bxjls,bxjlt,bxjmi,bxjne,
                bxjpl,bxjvc,bxjvs,bxle,bxlo,bxls,bxlt,bxmi,bxne,bxpl,bxvc,bxvs,cdp,
                cdp2,cdpal,cdpcc,cdpcs,cdpeq,cdpge,cdpgt,cdphi,cdphs,cdple,cdplo,
                cdpls,cdplt,cdpmi,cdpne,cdppl,cdpvc,cdpvs,clz,clzal,clzcc,clzcs,clzeq,
                clzge,clzgt,clzhi,clzhs,clzle,clzlo,clzls,clzlt,clzmi,clzne,clzpl,
                clzvc,clzvs,cmn,cmnal,cmncc,cmncs,cmneq,cmnge,cmngt,cmnhi,cmnhs,cmnle,
                cmnlo,cmnls,cmnlt,cmnmi,cmnne,cmnpl,cmnvc,cmnvs,cmp,cmpal,cmpcc,cmpcs,
                cmpeq,cmpge,cmpgt,cmphi,cmphs,cmple,cmplo,cmpls,cmplt,cmpmi,cmpne,
                cmppl,cmpvc,cmpvs,cps,cpsid,cpsie,cpy,cpyal,cpycc,cpycs,cpyeq,cpyge,
                cpygt,cpyhi,cpyhs,cpyle,cpylo,cpyls,cpylt,cpymi,cpyne,cpypl,cpyvc,
                cpyvs,eor,eoral,eorals,eorcc,eorccs,eorcs,eorcss,eoreq,eoreqs,eorge,
                eorges,eorgt,eorgts,eorhi,eorhis,eorhs,eorhss,eorle,eorles,eorlo,
                eorlos,eorls,eorlss,eorlt,eorlts,eormi,eormis,eorne,eornes,eorpl,
                eorpls,eors,eorvc,eorvcs,eorvs,eorvss,
                ldsh, ldsb,
                ldc,ldc2,ldcal,ldccc,ldccs,
                ldceq,ldcge,ldcgt,ldchi,ldchs,ldcle,ldclo,ldcls,ldclt,ldcmi,ldcne,
                ldcpl,ldcvc,ldcvs,ldmalda,ldmaldb,ldmalea,ldmaled,ldmalfa,ldmalfd,
                ldmalia,ldmalib,ldmccda,ldmccdb,ldmccea,ldmcced,ldmccfa,ldmccfd,
                ldmccia,ldmccib,ldmcsda,ldmcsdb,ldmcsea,ldmcsed,ldmcsfa,ldmcsfd,
                ldmcsia,ldmcsib,ldmda,ldmdb,ldmea,ldmed,ldmeqda,ldmeqdb,ldmeqea,
                ldmeqed,ldmeqfa,ldmeqfd,ldmeqia,ldmeqib,ldmfa,ldmfd,ldmgeda,ldmgedb,
                ldmgeea,ldmgeed,ldmgefa,ldmgefd,ldmgeia,ldmgeib,ldmgtda,ldmgtdb,
                ldmgtea,ldmgted,ldmgtfa,ldmgtfd,ldmgtia,ldmgtib,ldmhida,ldmhidb,
                ldmhiea,ldmhied,ldmhifa,ldmhifd,ldmhiia,ldmhiib,ldmhsda,ldmhsdb,
                ldmhsea,ldmhsed,ldmhsfa,ldmhsfd,ldmhsia,ldmhsib,ldmia,ldmib,ldmleda,
                ldmledb,ldmleea,ldmleed,ldmlefa,ldmlefd,ldmleia,ldmleib,ldmloda,
                ldmlodb,ldmloea,ldmloed,ldmlofa,ldmlofd,ldmloia,ldmloib,ldmlsda,
                ldmlsdb,ldmlsea,ldmlsed,ldmlsfa,ldmlsfd,ldmlsia,ldmlsib,ldmltda,
                ldmltdb,ldmltea,ldmlted,ldmltfa,ldmltfd,ldmltia,ldmltib,ldmmida,
                ldmmidb,ldmmiea,ldmmied,ldmmifa,ldmmifd,ldmmiia,ldmmiib,ldmneda,
                ldmnedb,ldmneea,ldmneed,ldmnefa,ldmnefd,ldmneia,ldmneib,ldmplda,
                ldmpldb,ldmplea,ldmpled,ldmplfa,ldmplfd,ldmplia,ldmplib,ldmvcda,
                ldmvcdb,ldmvcea,ldmvced,ldmvcfa,ldmvcfd,ldmvcia,ldmvcib,ldmvsda,
                ldmvsdb,ldmvsea,ldmvsed,ldmvsfa,ldmvsfd,ldmvsia,ldmvsib,ldr,ldral,
                ldralb,ldralbt,ldrald,ldralh,ldralsb,ldralsh,ldralt,ldrb,ldrbt,ldrcc,
                ldrccb,ldrccbt,ldrccd,ldrcch,ldrccsb,ldrccsh,ldrcct,ldrcs,ldrcsb,
                ldrcsbt,ldrcsd,ldrcsh,ldrcssb,ldrcssh,ldrcst,ldrd,ldreq,ldreqb,
                ldreqbt,ldreqd,ldreqh,ldreqsb,ldreqsh,ldreqt,ldrex,ldrexal,ldrexcc,
                ldrexcs,ldrexeq,ldrexge,ldrexgt,ldrexhi,ldrexhs,ldrexle,ldrexlo,
                ldrexls,ldrexlt,ldrexmi,ldrexne,ldrexpl,ldrexvc,ldrexvs,ldrge,ldrgeb,
                ldrgebt,ldrged,ldrgeh,ldrgesb,ldrgesh,ldrget,ldrgt,ldrgtb,ldrgtbt,
                ldrgtd,ldrgth,ldrgtsb,ldrgtsh,ldrgtt,ldrh,ldrhi,ldrhib,ldrhibt,ldrhid,
                ldrhih,ldrhisb,ldrhish,ldrhit,ldrhs,ldrhsb,ldrhsbt,ldrhsd,ldrhsh,
                ldrhssb,ldrhssh,ldrhst,ldrle,ldrleb,ldrlebt,ldrled,ldrleh,ldrlesb,
                ldrlesh,ldrlet,ldrlo,ldrlob,ldrlobt,ldrlod,ldrloh,ldrlosb,ldrlosh,
                ldrlot,ldrls,ldrlsb,ldrlsbt,ldrlsd,ldrlsh,ldrlssb,ldrlssh,ldrlst,
                ldrlt,ldrltb,ldrltbt,ldrltd,ldrlth,ldrltsb,ldrltsh,ldrltt,ldrmi,
                ldrmib,ldrmibt,ldrmid,ldrmih,ldrmisb,ldrmish,ldrmit,ldrne,ldrneb,
                ldrnebt,ldrned,ldrneh,ldrnesb,ldrnesh,ldrnet,ldrpl,ldrplb,ldrplbt,
                ldrpld,ldrplh,ldrplsb,ldrplsh,ldrplt,ldrsb,ldrsh,ldrt,ldrvc,ldrvcb,
                ldrvcbt,ldrvcd,ldrvch,ldrvcsb,ldrvcsh,ldrvct,ldrvs,ldrvsb,ldrvsbt,
                ldrvsd,ldrvsh,ldrvssb,ldrvssh,ldrvst,lsl,lsls,lsr,lsrs,mar,maral,marcc,marcs,
                mareq,
                marge,margt,marhi,marhs,marle,marlo,marls,marlt,marmi,marne,marpl,
                marvc,marvs,mcr,mcr2,mcral,mcrcc,mcrcs,mcreq,mcrge,mcrgt,mcrhi,mcrhs,
                mcrle,mcrlo,mcrls,mcrlt,mcrmi,mcrne,mcrpl,mcrr,mcrr2,mcrral,mcrrcc,
                mcrrcs,mcrreq,mcrrge,mcrrgt,mcrrhi,mcrrhs,mcrrle,mcrrlo,mcrrls,mcrrlt,
                mcrrmi,mcrrne,mcrrpl,mcrrvc,mcrrvs,mcrvc,mcrvs,mia,miaal,miacc,miacs,
                miaeq,miage,miagt,miahi,miahs,miale,mialo,mials,mialt,miami,miane,
                miaph,miaphal,miaphcc,miaphcs,miapheq,miaphge,miaphgt,miaphhi,miaphhs,
                miaphle,miaphlo,miaphls,miaphlt,miaphmi,miaphne,miaphpl,miaphvc,
                miaphvs,miapl,miavc,miavs,miaxy,miaxyal,miaxycc,miaxycs,miaxyeq,
                miaxyge,miaxygt,miaxyhi,miaxyhs,miaxyle,miaxylo,miaxyls,miaxylt,
                miaxymi,miaxyne,miaxypl,miaxyvc,miaxyvs,mla,mlaal,mlaals,mlacc,mlaccs,
                mlacs,mlacss,mlaeq,mlaeqs,mlage,mlages,mlagt,mlagts,mlahi,mlahis,
                mlahs,mlahss,mlale,mlales,mlalo,mlalos,mlals,mlalss,mlalt,mlalts,
                mlami,mlamis,mlane,mlanes,mlapl,mlapls,mlas,mlavc,mlavcs,mlavs,mlavss,
                mov,moval,movals,movcc,movccs,movcs,movcss,moveq,moveqs,movge,movges,
                movgt,movgts,movhi,movhis,movhs,movhss,movle,movles,movlo,movlos,
                movls,movlss,movlt,movlts,movmi,movmis,movne,movnes,movpl,movpls,movs,
                movvc,movvcs,movvs,movvss,mra,mraal,mracc,mracs,mraeq,mrage,mragt,
                mrahi,mrahs,mrale,mralo,mrals,mralt,mrami,mrane,mrapl,mravc,mravs,mrc,
                mrc2,mrcal,mrccc,mrccs,mrceq,mrcge,mrcgt,mrchi,mrchs,mrcle,mrclo,
                mrcls,mrclt,mrcmi,mrcne,mrcpl,mrcvc,mrcvs,mrrc,mrrc2,mrrcal,mrrccc,
                mrrccs,mrrceq,mrrcge,mrrcgt,mrrchi,mrrchs,mrrcle,mrrclo,mrrcls,mrrclt,
                mrrcmi,mrrcne,mrrcpl,mrrcvc,mrrcvs,mrs,mrsal,mrscc,mrscs,mrseq,mrsge,
                mrsgt,mrshi,mrshs,mrsle,mrslo,mrsls,mrslt,mrsmi,mrsne,mrspl,mrsvc,
                mrsvs,msr,msral,msrcc,msrcs,msreq,msrge,msrgt,msrhi,msrhs,msrle,msrlo,
                msrls,msrlt,msrmi,msrne,msrpl,msrvc,msrvs,mul,mulal,mulals,mulcc,
                mulccs,mulcs,mulcss,muleq,muleqs,mulge,mulges,mulgt,mulgts,mulhi,
                mulhis,mulhs,mulhss,mulle,mulles,mullo,mullos,mulls,mullss,mullt,
                mullts,mulmi,mulmis,mulne,mulnes,mulpl,mulpls,muls,mulvc,mulvcs,mulvs,
                mulvss,mvn,mvnal,mvnals,mvncc,mvnccs,mvncs,mvncss,mvneq,mvneqs,mvnge,
                mvnges,mvngt,mvngts,mvnhi,mvnhis,mvnhs,mvnhss,mvnle,mvnles,mvnlo,
                mvnlos,mvnls,mvnlss,mvnlt,mvnlts,mvnmi,mvnmis,mvnne,mvnnes,mvnpl,
                mvnpls,mvns,mvnvc,mvnvcs,mvnvs,mvnvss,neg,nop,orr,orral,orrals,orrcc,
                orrccs,orrcs,orrcss,orreq,orreqs,orrge,orrges,orrgt,orrgts,orrhi,
                orrhis,orrhs,orrhss,orrle,orrles,orrlo,orrlos,orrls,orrlss,orrlt,
                orrlts,orrmi,orrmis,orrne,orrnes,orrpl,orrpls,orrs,orrvc,orrvcs,orrvs,
                orrvss,pkhbt,pkhbtal,pkhbtcc,pkhbtcs,pkhbteq,pkhbtge,pkhbtgt,pkhbthi,
                pkhbths,pkhbtle,pkhbtlo,pkhbtls,pkhbtlt,pkhbtmi,pkhbtne,pkhbtpl,
                pkhbtvc,pkhbtvs,pkhtb,pkhtbal,pkhtbcc,pkhtbcs,pkhtbeq,pkhtbge,pkhtbgt,
                pkhtbhi,pkhtbhs,pkhtble,pkhtblo,pkhtbls,pkhtblt,pkhtbmi,pkhtbne,
                pkhtbpl,pkhtbvc,pkhtbvs,pld,pop,popal,popcc,popcs,popeq,popge,popgt,
                pophi,pophs,pople,poplo,popls,poplt,popmi,popne,poppl,popvc,popvs,
                push,pushal,pushcc,pushcs,pusheq,pushge,pushgt,pushhi,pushhs,pushle,
                pushlo,pushls,pushlt,pushmi,pushne,pushpl,pushvc,pushvs,qadd,qadd16,
                qadd16al,qadd16cc,qadd16cs,qadd16eq,qadd16ge,qadd16gt,qadd16hi,
                qadd16hs,qadd16le,qadd16lo,qadd16ls,qadd16lt,qadd16mi,qadd16ne,
                qadd16pl,qadd16vc,qadd16vs,qadd8,qadd8al,qadd8cc,qadd8cs,qadd8eq,
                qadd8ge,qadd8gt,qadd8hi,qadd8hs,qadd8le,qadd8lo,qadd8ls,qadd8lt,
                qadd8mi,qadd8ne,qadd8pl,qadd8vc,qadd8vs,qaddal,qaddcc,qaddcs,qaddeq,
                qaddge,qaddgt,qaddhi,qaddhs,qaddle,qaddlo,qaddls,qaddlt,qaddmi,qaddne,
                qaddpl,qaddsubx,qaddsubxal,qaddsubxcc,qaddsubxcs,qaddsubxeq,
                qaddsubxge,qaddsubxgt,qaddsubxhi,qaddsubxhs,qaddsubxle,qaddsubxlo,
                qaddsubxls,qaddsubxlt,qaddsubxmi,qaddsubxne,qaddsubxpl,qaddsubxvc,
                qaddsubxvs,qaddvc,qaddvs,qdadd,qdaddal,qdaddcc,qdaddcs,qdaddeq,
                qdaddge,qdaddgt,qdaddhi,qdaddhs,qdaddle,qdaddlo,qdaddls,qdaddlt,
                qdaddmi,qdaddne,qdaddpl,qdaddvc,qdaddvs,qdsub,qdsubal,qdsubcc,qdsubcs,
                qdsubeq,qdsubge,qdsubgt,qdsubhi,qdsubhs,qdsuble,qdsublo,qdsubls,
                qdsublt,qdsubmi,qdsubne,qdsubpl,qdsubvc,qdsubvs,qsub,qsub16,qsub16al,
                qsub16cc,qsub16cs,qsub16eq,qsub16ge,qsub16gt,qsub16hi,qsub16hs,
                qsub16le,qsub16lo,qsub16ls,qsub16lt,qsub16mi,qsub16ne,qsub16pl,
                qsub16vc,qsub16vs,qsub8,qsub8al,qsub8cc,qsub8cs,qsub8eq,qsub8ge,
                qsub8gt,qsub8hi,qsub8hs,qsub8le,qsub8lo,qsub8ls,qsub8lt,qsub8mi,
                qsub8ne,qsub8pl,qsub8vc,qsub8vs,qsubaddx,qsubaddxal,qsubaddxcc,
                qsubaddxcs,qsubaddxeq,qsubaddxge,qsubaddxgt,qsubaddxhi,qsubaddxhs,
                qsubaddxle,qsubaddxlo,qsubaddxls,qsubaddxlt,qsubaddxmi,qsubaddxne,
                qsubaddxpl,qsubaddxvc,qsubaddxvs,qsubal,qsubcc,qsubcs,qsubeq,qsubge,
                qsubgt,qsubhi,qsubhs,qsuble,qsublo,qsubls,qsublt,qsubmi,qsubne,qsubpl,
                qsubvc,qsubvs,rev,rev16,rev16al,rev16cc,rev16cs,rev16eq,rev16ge,
                rev16gt,rev16hi,rev16hs,rev16le,rev16lo,rev16ls,rev16lt,rev16mi,
                rev16ne,rev16pl,rev16vc,rev16vs,reval,revcc,revcs,reveq,revge,revgt,
                revhi,revhs,revle,revlo,revls,revlt,revmi,revne,revpl,revsh,revshal,
                revshcc,revshcs,revsheq,revshge,revshgt,revshhi,revshhs,revshle,
                revshlo,revshls,revshlt,revshmi,revshne,revshpl,revshvc,revshvs,revvc,
                revvs,rfeda,rfedb,rfeea,rfeed,rfefa,rfefd,rfeia,rfeib,rsb,rsbal,
                rsbals,rsbcc,rsbccs,rsbcs,rsbcss,rsbeq,rsbeqs,rsbge,rsbges,rsbgt,
                rsbgts,rsbhi,rsbhis,rsbhs,rsbhss,rsble,rsbles,rsblo,rsblos,rsbls,
                rsblss,rsblt,rsblts,rsbmi,rsbmis,rsbne,rsbnes,rsbpl,rsbpls,rsbs,rsbvc,
                rsbvcs,rsbvs,rsbvss,rsc,rscal,rscals,rsccc,rscccs,rsccs,rsccss,rsceq,
                rsceqs,rscge,rscges,rscgt,rscgts,rschi,rschis,rschs,rschss,rscle,
                rscles,rsclo,rsclos,rscls,rsclss,rsclt,rsclts,rscmi,rscmis,rscne,
                rscnes,rscpl,rscpls,rscs,rscvc,rscvcs,rscvs,rscvss,sadd16,sadd16al,
                sadd16cc,sadd16cs,sadd16eq,sadd16ge,sadd16gt,sadd16hi,sadd16hs,
                sadd16le,sadd16lo,sadd16ls,sadd16lt,sadd16mi,sadd16ne,sadd16pl,
                sadd16vc,sadd16vs,sadd8,sadd8al,sadd8cc,sadd8cs,sadd8eq,sadd8ge,
                sadd8gt,sadd8hi,sadd8hs,sadd8le,sadd8lo,sadd8ls,sadd8lt,sadd8mi,
                sadd8ne,sadd8pl,sadd8vc,sadd8vs,saddsubx,saddsubxal,saddsubxcc,
                saddsubxcs,saddsubxeq,saddsubxge,saddsubxgt,saddsubxhi,saddsubxhs,
                saddsubxle,saddsubxlo,saddsubxls,saddsubxlt,saddsubxmi,saddsubxne,
                saddsubxpl,saddsubxvc,saddsubxvs,sbc,sbcal,sbcals,sbccc,sbcccs,sbccs,
                sbccss,sbceq,sbceqs,sbcge,sbcges,sbcgt,sbcgts,sbchi,sbchis,sbchs,
                sbchss,sbcle,sbcles,sbclo,sbclos,sbcls,sbclss,sbclt,sbclts,sbcmi,
                sbcmis,sbcne,sbcnes,sbcpl,sbcpls,sbcs,sbcvc,sbcvcs,sbcvs,sbcvss,sel,
                selal,selcc,selcs,seleq,selge,selgt,selhi,selhs,selle,sello,sells,
                sellt,selmi,selne,selpl,selvc,selvs,setend,shadd16,shadd16al,
                shadd16cc,shadd16cs,shadd16eq,shadd16ge,shadd16gt,shadd16hi,shadd16hs,
                shadd16le,shadd16lo,shadd16ls,shadd16lt,shadd16mi,shadd16ne,shadd16pl,
                shadd16vc,shadd16vs,shadd8,shadd8al,shadd8cc,shadd8cs,shadd8eq,
                shadd8ge,shadd8gt,shadd8hi,shadd8hs,shadd8le,shadd8lo,shadd8ls,
                shadd8lt,shadd8mi,shadd8ne,shadd8pl,shadd8vc,shadd8vs,shaddsubx,
                shaddsubxal,shaddsubxcc,shaddsubxcs,shaddsubxeq,shaddsubxge,
                shaddsubxgt,shaddsubxhi,shaddsubxhs,shaddsubxle,shaddsubxlo,
                shaddsubxls,shaddsubxlt,shaddsubxmi,shaddsubxne,shaddsubxpl,
                shaddsubxvc,shaddsubxvs,shsub16,shsub16al,shsub16cc,shsub16cs,
                shsub16eq,shsub16ge,shsub16gt,shsub16hi,shsub16hs,shsub16le,shsub16lo,
                shsub16ls,shsub16lt,shsub16mi,shsub16ne,shsub16pl,shsub16vc,shsub16vs,
                shsub8,shsub8al,shsub8cc,shsub8cs,shsub8eq,shsub8ge,shsub8gt,shsub8hi,
                shsub8hs,shsub8le,shsub8lo,shsub8ls,shsub8lt,shsub8mi,shsub8ne,
                shsub8pl,shsub8vc,shsub8vs,shsubaddx,shsubaddxal,shsubaddxcc,
                shsubaddxcs,shsubaddxeq,shsubaddxge,shsubaddxgt,shsubaddxhi,
                shsubaddxhs,shsubaddxle,shsubaddxlo,shsubaddxls,shsubaddxlt,
                shsubaddxmi,shsubaddxne,shsubaddxpl,shsubaddxvc,shsubaddxvs,smlad,
                smladal,smladcc,smladcs,smladeq,smladge,smladgt,smladhi,smladhs,
                smladle,smladlo,smladls,smladlt,smladmi,smladne,smladpl,smladvc,
                smladvs,smladx,smladxal,smladxcc,smladxcs,smladxeq,smladxge,smladxgt,
                smladxhi,smladxhs,smladxle,smladxlo,smladxls,smladxlt,smladxmi,
                smladxne,smladxpl,smladxvc,smladxvs,smlal,smlalal,smlalals,smlalcc,
                smlalccs,smlalcs,smlalcss,smlald,smlaldal,smlaldcc,smlaldcs,smlaldeq,
                smlaldge,smlaldgt,smlaldhi,smlaldhs,smlaldle,smlaldlo,smlaldls,
                smlaldlt,smlaldmi,smlaldne,smlaldpl,smlaldvc,smlaldvs,smlaldx,
                smlaldxal,smlaldxcc,smlaldxcs,smlaldxeq,smlaldxge,smlaldxgt,smlaldxhi,
                smlaldxhs,smlaldxle,smlaldxlo,smlaldxls,smlaldxlt,smlaldxmi,smlaldxne,
                smlaldxpl,smlaldxvc,smlaldxvs,smlaleq,smlaleqs,smlalge,smlalges,
                smlalgt,smlalgts,smlalhi,smlalhis,smlalhs,smlalhss,smlalle,smlalles,
                smlallo,smlallos,smlalls,smlallss,smlallt,smlallts,smlalmi,smlalmis,
                smlalne,smlalnes,smlalpl,smlalpls,smlals,smlalvc,smlalvcs,smlalvs,
                smlalvss,smlalxy,smlalxyal,smlalxycc,smlalxycs,smlalxyeq,smlalxyge,
                smlalxygt,smlalxyhi,smlalxyhs,smlalxyle,smlalxylo,smlalxyls,smlalxylt,
                smlalxymi,smlalxyne,smlalxypl,smlalxyvc,smlalxyvs,smlawy,smlawyal,
                smlawycc,smlawycs,smlawyeq,smlawyge,smlawygt,smlawyhi,smlawyhs,
                smlawyle,smlawylo,smlawyls,smlawylt,smlawymi,smlawyne,smlawypl,
                smlawyvc,smlawyvs,smlaxy,smlaxyal,smlaxycc,smlaxycs,smlaxyeq,smlaxyge,
                smlaxygt,smlaxyhi,smlaxyhs,smlaxyle,smlaxylo,smlaxyls,smlaxylt,
                smlaxymi,smlaxyne,smlaxypl,smlaxyvc,smlaxyvs,smlsd,smlsdal,smlsdcc,
                smlsdcs,smlsdeq,smlsdge,smlsdgt,smlsdhi,smlsdhs,smlsdle,smlsdlo,
                smlsdls,smlsdlt,smlsdmi,smlsdne,smlsdpl,smlsdvc,smlsdvs,smlsdx,
                smlsdxal,smlsdxcc,smlsdxcs,smlsdxeq,smlsdxge,smlsdxgt,smlsdxhi,
                smlsdxhs,smlsdxle,smlsdxlo,smlsdxls,smlsdxlt,smlsdxmi,smlsdxne,
                smlsdxpl,smlsdxvc,smlsdxvs,smlsld,smlsldal,smlsldcc,smlsldcs,smlsldeq,
                smlsldge,smlsldgt,smlsldhi,smlsldhs,smlsldle,smlsldlo,smlsldls,
                smlsldlt,smlsldmi,smlsldne,smlsldpl,smlsldvc,smlsldvs,smlsldx,
                smlsldxal,smlsldxcc,smlsldxcs,smlsldxeq,smlsldxge,smlsldxgt,smlsldxhi,
                smlsldxhs,smlsldxle,smlsldxlo,smlsldxls,smlsldxlt,smlsldxmi,smlsldxne,
                smlsldxpl,smlsldxvc,smlsldxvs,smmla,smmlaal,smmlacc,smmlacs,smmlaeq,
                smmlage,smmlagt,smmlahi,smmlahs,smmlale,smmlalo,smmlals,smmlalt,
                smmlami,smmlane,smmlapl,smmlar,smmlaral,smmlarcc,smmlarcs,smmlareq,
                smmlarge,smmlargt,smmlarhi,smmlarhs,smmlarle,smmlarlo,smmlarls,
                smmlarlt,smmlarmi,smmlarne,smmlarpl,smmlarvc,smmlarvs,smmlavc,smmlavs,
                smmls,smmlsal,smmlscc,smmlscs,smmlseq,smmlsge,smmlsgt,smmlshi,smmlshs,
                smmlsle,smmlslo,smmlsls,smmlslt,smmlsmi,smmlsne,smmlspl,smmlsr,
                smmlsral,smmlsrcc,smmlsrcs,smmlsreq,smmlsrge,smmlsrgt,smmlsrhi,
                smmlsrhs,smmlsrle,smmlsrlo,smmlsrls,smmlsrlt,smmlsrmi,smmlsrne,
                smmlsrpl,smmlsrvc,smmlsrvs,smmlsvc,smmlsvs,smmul,smmulal,smmulcc,
                smmulcs,smmuleq,smmulge,smmulgt,smmulhi,smmulhs,smmulle,smmullo,
                smmulls,smmullt,smmulmi,smmulne,smmulpl,smmulr,smmulral,smmulrcc,
                smmulrcs,smmulreq,smmulrge,smmulrgt,smmulrhi,smmulrhs,smmulrle,
                smmulrlo,smmulrls,smmulrlt,smmulrmi,smmulrne,smmulrpl,smmulrvc,
                smmulrvs,smmulvc,smmulvs,smuad,smuadal,smuadcc,smuadcs,smuadeq,
                smuadge,smuadgt,smuadhi,smuadhs,smuadle,smuadlo,smuadls,smuadlt,
                smuadmi,smuadne,smuadpl,smuadvc,smuadvs,smuadx,smuadxal,smuadxcc,
                smuadxcs,smuadxeq,smuadxge,smuadxgt,smuadxhi,smuadxhs,smuadxle,
                smuadxlo,smuadxls,smuadxlt,smuadxmi,smuadxne,smuadxpl,smuadxvc,
                smuadxvs,smull,smullal,smullals,smullcc,smullccs,smullcs,smullcss,
                smulleq,smulleqs,smullge,smullges,smullgt,smullgts,smullhi,smullhis,
                smullhs,smullhss,smullle,smullles,smulllo,smulllos,smullls,smulllss,
                smulllt,smulllts,smullmi,smullmis,smullne,smullnes,smullpl,smullpls,
                smulls,smullvc,smullvcs,smullvs,smullvss,smulwy,smulwyal,smulwycc,
                smulwycs,smulwyeq,smulwyge,smulwygt,smulwyhi,smulwyhs,smulwyle,
                smulwylo,smulwyls,smulwylt,smulwymi,smulwyne,smulwypl,smulwyvc,
                smulwyvs,smulxy,smulxyal,smulxycc,smulxycs,smulxyeq,smulxyge,smulxygt,
                smulxyhi,smulxyhs,smulxyle,smulxylo,smulxyls,smulxylt,smulxymi,
                smulxyne,smulxypl,smulxyvc,smulxyvs,smusd,smusdal,smusdcc,smusdcs,
                smusdeq,smusdge,smusdgt,smusdhi,smusdhs,smusdle,smusdlo,smusdls,
                smusdlt,smusdmi,smusdne,smusdpl,smusdvc,smusdvs,smusdx,smusdxal,
                smusdxcc,smusdxcs,smusdxeq,smusdxge,smusdxgt,smusdxhi,smusdxhs,
                smusdxle,smusdxlo,smusdxls,smusdxlt,smusdxmi,smusdxne,smusdxpl,
                smusdxvc,smusdxvs,srsda,srsdb,srsea,srsed,srsfa,srsfd,srsia,srsib,
                ssat,ssat16,ssat16al,ssat16cc,ssat16cs,ssat16eq,ssat16ge,ssat16gt,
                ssat16hi,ssat16hs,ssat16le,ssat16lo,ssat16ls,ssat16lt,ssat16mi,
                ssat16ne,ssat16pl,ssat16vc,ssat16vs,ssatal,ssatcc,ssatcs,ssateq,
                ssatge,ssatgt,ssathi,ssaths,ssatle,ssatlo,ssatls,ssatlt,ssatmi,ssatne,
                ssatpl,ssatvc,ssatvs,ssub16,ssub16al,ssub16cc,ssub16cs,ssub16eq,
                ssub16ge,ssub16gt,ssub16hi,ssub16hs,ssub16le,ssub16lo,ssub16ls,
                ssub16lt,ssub16mi,ssub16ne,ssub16pl,ssub16vc,ssub16vs,ssub8,ssub8al,
                ssub8cc,ssub8cs,ssub8eq,ssub8ge,ssub8gt,ssub8hi,ssub8hs,ssub8le,
                ssub8lo,ssub8ls,ssub8lt,ssub8mi,ssub8ne,ssub8pl,ssub8vc,ssub8vs,
                ssubaddx,ssubaddxal,ssubaddxcc,ssubaddxcs,ssubaddxeq,ssubaddxge,
                ssubaddxgt,ssubaddxhi,ssubaddxhs,ssubaddxle,ssubaddxlo,ssubaddxls,
                ssubaddxlt,ssubaddxmi,ssubaddxne,ssubaddxpl,ssubaddxvc,ssubaddxvs,stc,
                stc2,stcal,stccc,stccs,stceq,stcge,stcgt,stchi,stchs,stcle,stclo,
                stcls,stclt,stcmi,stcne,stcpl,stcvc,stcvs,stmalda,stmaldb,stmalea,
                stmaled,stmalfa,stmalfd,stmalia,stmalib,stmccda,stmccdb,stmccea,
                stmcced,stmccfa,stmccfd,stmccia,stmccib,stmcsda,stmcsdb,stmcsea,
                stmcsed,stmcsfa,stmcsfd,stmcsia,stmcsib,stmda,stmdb,stmea,stmed,
                stmeqda,stmeqdb,stmeqea,stmeqed,stmeqfa,stmeqfd,stmeqia,stmeqib,stmfa,
                stmfd,stmgeda,stmgedb,stmgeea,stmgeed,stmgefa,stmgefd,stmgeia,stmgeib,
                stmgtda,stmgtdb,stmgtea,stmgted,stmgtfa,stmgtfd,stmgtia,stmgtib,
                stmhida,stmhidb,stmhiea,stmhied,stmhifa,stmhifd,stmhiia,stmhiib,
                stmhsda,stmhsdb,stmhsea,stmhsed,stmhsfa,stmhsfd,stmhsia,stmhsib,stmia,
                stmib,stmleda,stmledb,stmleea,stmleed,stmlefa,stmlefd,stmleia,stmleib,
                stmloda,stmlodb,stmloea,stmloed,stmlofa,stmlofd,stmloia,stmloib,
                stmlsda,stmlsdb,stmlsea,stmlsed,stmlsfa,stmlsfd,stmlsia,stmlsib,
                stmltda,stmltdb,stmltea,stmlted,stmltfa,stmltfd,stmltia,stmltib,
                stmmida,stmmidb,stmmiea,stmmied,stmmifa,stmmifd,stmmiia,stmmiib,
                stmneda,stmnedb,stmneea,stmneed,stmnefa,stmnefd,stmneia,stmneib,
                stmplda,stmpldb,stmplea,stmpled,stmplfa,stmplfd,stmplia,stmplib,
                stmvcda,stmvcdb,stmvcea,stmvced,stmvcfa,stmvcfd,stmvcia,stmvcib,
                stmvsda,stmvsdb,stmvsea,stmvsed,stmvsfa,stmvsfd,stmvsia,stmvsib,str,
                stral,stralb,stralbt,strald,stralh,stralt,strb,strbt,strcc,strccb,
                strccbt,strccd,strcch,strcct,strcs,strcsb,strcsbt,strcsd,strcsh,
                strcst,strd,streq,streqb,streqbt,streqd,streqh,streqt,strex,strexal,
                strexcc,strexcs,strexeq,strexge,strexgt,strexhi,strexhs,strexle,
                strexlo,strexls,strexlt,strexmi,strexne,strexpl,strexvc,strexvs,strge,
                strgeb,strgebt,strged,strgeh,strget,strgt,strgtb,strgtbt,strgtd,
                strgth,strgtt,strh,strhi,strhib,strhibt,strhid,strhih,strhit,strhs,
                strhsb,strhsbt,strhsd,strhsh,strhst,strle,strleb,strlebt,strled,
                strleh,strlet,strlo,strlob,strlobt,strlod,strloh,strlot,strls,strlsb,
                strlsbt,strlsd,strlsh,strlst,strlt,strltb,strltbt,strltd,strlth,
                strltt,strmi,strmib,strmibt,strmid,strmih,strmit,strne,strneb,strnebt,
                strned,strneh,strnet,strpl,strplb,strplbt,strpld,strplh,strplt,strt,
                strvc,strvcb,strvcbt,strvcd,strvch,strvct,strvs,strvsb,strvsbt,strvsd,
                strvsh,strvst,sub,subal,subals,subcc,subccs,subcs,subcss,subeq,subeqs,
                subge,subges,subgt,subgts,subhi,subhis,subhs,subhss,suble,subles,
                sublo,sublos,subls,sublss,sublt,sublts,submi,submis,subne,subnes,
                subpl,subpls,subs,subvc,subvcs,subvs,subvss,swi,swial,swicc,swics,
                swieq,swige,swigt,swihi,swihs,swile,swilo,swils,swilt,swimi,swine,
                swipl,swivc,swivs,swp,swpal,swpalb,swpb,swpcc,swpccb,swpcs,swpcsb,
                swpeq,swpeqb,swpge,swpgeb,swpgt,swpgtb,swphi,swphib,swphs,swphsb,
                swple,swpleb,swplo,swplob,swpls,swplsb,swplt,swpltb,swpmi,swpmib,
                swpne,swpneb,swppl,swpplb,swpvc,swpvcb,swpvs,swpvsb,sxtab,sxtab16,
                sxtab16al,sxtab16cc,sxtab16cs,sxtab16eq,sxtab16ge,sxtab16gt,sxtab16hi,
                sxtab16hs,sxtab16le,sxtab16lo,sxtab16ls,sxtab16lt,sxtab16mi,sxtab16ne,
                sxtab16pl,sxtab16vc,sxtab16vs,sxtabal,sxtabcc,sxtabcs,sxtabeq,sxtabge,
                sxtabgt,sxtabhi,sxtabhs,sxtable,sxtablo,sxtabls,sxtablt,sxtabmi,
                sxtabne,sxtabpl,sxtabvc,sxtabvs,sxtah,sxtahal,sxtahcc,sxtahcs,sxtaheq,
                sxtahge,sxtahgt,sxtahhi,sxtahhs,sxtahle,sxtahlo,sxtahls,sxtahlt,
                sxtahmi,sxtahne,sxtahpl,sxtahvc,sxtahvs,sxtb,sxtb16,sxtb16al,sxtb16cc,
                sxtb16cs,sxtb16eq,sxtb16ge,sxtb16gt,sxtb16hi,sxtb16hs,sxtb16le,
                sxtb16lo,sxtb16ls,sxtb16lt,sxtb16mi,sxtb16ne,sxtb16pl,sxtb16vc,
                sxtb16vs,sxtbal,sxtbcc,sxtbcs,sxtbeq,sxtbge,sxtbgt,sxtbhi,sxtbhs,
                sxtble,sxtblo,sxtbls,sxtblt,sxtbmi,sxtbne,sxtbpl,sxtbvc,sxtbvs,sxth,
                sxthal,sxthcc,sxthcs,sxtheq,sxthge,sxthgt,sxthhi,sxthhs,sxthle,sxthlo,
                sxthls,sxthlt,sxthmi,sxthne,sxthpl,sxthvc,sxthvs,teq,teqal,teqcc,
                teqcs,teqeq,teqge,teqgt,teqhi,teqhs,teqle,teqlo,teqls,teqlt,teqmi,
                teqne,teqpl,teqvc,teqvs,tst,tstal,tstcc,tstcs,tsteq,tstge,tstgt,tsthi,
                tsths,tstle,tstlo,tstls,tstlt,tstmi,tstne,tstpl,tstvc,tstvs,uadd16,
                uadd16al,uadd16cc,uadd16cs,uadd16eq,uadd16ge,uadd16gt,uadd16hi,
                uadd16hs,uadd16le,uadd16lo,uadd16ls,uadd16lt,uadd16mi,uadd16ne,
                uadd16pl,uadd16vc,uadd16vs,uadd8,uadd8al,uadd8cc,uadd8cs,uadd8eq,
                uadd8ge,uadd8gt,uadd8hi,uadd8hs,uadd8le,uadd8lo,uadd8ls,uadd8lt,
                uadd8mi,uadd8ne,uadd8pl,uadd8vc,uadd8vs,uaddsubx,uaddsubxal,
                uaddsubxcc,uaddsubxcs,uaddsubxeq,uaddsubxge,uaddsubxgt,uaddsubxhi,
                uaddsubxhs,uaddsubxle,uaddsubxlo,uaddsubxls,uaddsubxlt,uaddsubxmi,
                uaddsubxne,uaddsubxpl,uaddsubxvc,uaddsubxvs,uhadd16,uhadd16al,
                uhadd16cc,uhadd16cs,uhadd16eq,uhadd16ge,uhadd16gt,uhadd16hi,uhadd16hs,
                uhadd16le,uhadd16lo,uhadd16ls,uhadd16lt,uhadd16mi,uhadd16ne,uhadd16pl,
                uhadd16vc,uhadd16vs,uhadd8,uhadd8al,uhadd8cc,uhadd8cs,uhadd8eq,
                uhadd8ge,uhadd8gt,uhadd8hi,uhadd8hs,uhadd8le,uhadd8lo,uhadd8ls,
                uhadd8lt,uhadd8mi,uhadd8ne,uhadd8pl,uhadd8vc,uhadd8vs,uhaddsubx,
                uhaddsubxal,uhaddsubxcc,uhaddsubxcs,uhaddsubxeq,uhaddsubxge,
                uhaddsubxgt,uhaddsubxhi,uhaddsubxhs,uhaddsubxle,uhaddsubxlo,
                uhaddsubxls,uhaddsubxlt,uhaddsubxmi,uhaddsubxne,uhaddsubxpl,
                uhaddsubxvc,uhaddsubxvs,uhsub16,uhsub16al,uhsub16cc,uhsub16cs,
                uhsub16eq,uhsub16ge,uhsub16gt,uhsub16hi,uhsub16hs,uhsub16le,uhsub16lo,
                uhsub16ls,uhsub16lt,uhsub16mi,uhsub16ne,uhsub16pl,uhsub16vc,uhsub16vs,
                uhsub8,uhsub8al,uhsub8cc,uhsub8cs,uhsub8eq,uhsub8ge,uhsub8gt,uhsub8hi,
                uhsub8hs,uhsub8le,uhsub8lo,uhsub8ls,uhsub8lt,uhsub8mi,uhsub8ne,
                uhsub8pl,uhsub8vc,uhsub8vs,uhsubaddx,uhsubaddxal,uhsubaddxcc,
                uhsubaddxcs,uhsubaddxeq,uhsubaddxge,uhsubaddxgt,uhsubaddxhi,
                uhsubaddxhs,uhsubaddxle,uhsubaddxlo,uhsubaddxls,uhsubaddxlt,
                uhsubaddxmi,uhsubaddxne,uhsubaddxpl,uhsubaddxvc,uhsubaddxvs,umaal,
                umaalal,umaalcc,umaalcs,umaaleq,umaalge,umaalgt,umaalhi,umaalhs,
                umaalle,umaallo,umaalls,umaallt,umaalmi,umaalne,umaalpl,umaalvc,
                umaalvs,umlal,umlalal,umlalals,umlalcc,umlalccs,umlalcs,umlalcss,
                umlaleq,umlaleqs,umlalge,umlalges,umlalgt,umlalgts,umlalhi,umlalhis,
                umlalhs,umlalhss,umlalle,umlalles,umlallo,umlallos,umlalls,umlallss,
                umlallt,umlallts,umlalmi,umlalmis,umlalne,umlalnes,umlalpl,umlalpls,
                umlals,umlalvc,umlalvcs,umlalvs,umlalvss,umull,umullal,umullals,
                umullcc,umullccs,umullcs,umullcss,umulleq,umulleqs,umullge,umullges,
                umullgt,umullgts,umullhi,umullhis,umullhs,umullhss,umullle,umullles,
                umulllo,umulllos,umullls,umulllss,umulllt,umulllts,umullmi,umullmis,
                umullne,umullnes,umullpl,umullpls,umulls,umullvc,umullvcs,umullvs,
                umullvss,uqadd16,uqadd16al,uqadd16cc,uqadd16cs,uqadd16eq,uqadd16ge,
                uqadd16gt,uqadd16hi,uqadd16hs,uqadd16le,uqadd16lo,uqadd16ls,uqadd16lt,
                uqadd16mi,uqadd16ne,uqadd16pl,uqadd16vc,uqadd16vs,uqadd8,uqadd8al,
                uqadd8cc,uqadd8cs,uqadd8eq,uqadd8ge,uqadd8gt,uqadd8hi,uqadd8hs,
                uqadd8le,uqadd8lo,uqadd8ls,uqadd8lt,uqadd8mi,uqadd8ne,uqadd8pl,
                uqadd8vc,uqadd8vs,uqaddsubx,uqaddsubxal,uqaddsubxcc,uqaddsubxcs,
                uqaddsubxeq,uqaddsubxge,uqaddsubxgt,uqaddsubxhi,uqaddsubxhs,
                uqaddsubxle,uqaddsubxlo,uqaddsubxls,uqaddsubxlt,uqaddsubxmi,
                uqaddsubxne,uqaddsubxpl,uqaddsubxvc,uqaddsubxvs,uqsub16,uqsub16al,
                uqsub16cc,uqsub16cs,uqsub16eq,uqsub16ge,uqsub16gt,uqsub16hi,uqsub16hs,
                uqsub16le,uqsub16lo,uqsub16ls,uqsub16lt,uqsub16mi,uqsub16ne,uqsub16pl,
                uqsub16vc,uqsub16vs,uqsub8,uqsub8al,uqsub8cc,uqsub8cs,uqsub8eq,
                uqsub8ge,uqsub8gt,uqsub8hi,uqsub8hs,uqsub8le,uqsub8lo,uqsub8ls,
                uqsub8lt,uqsub8mi,uqsub8ne,uqsub8pl,uqsub8vc,uqsub8vs,uqsubaddx,
                uqsubaddxal,uqsubaddxcc,uqsubaddxcs,uqsubaddxeq,uqsubaddxge,
                uqsubaddxgt,uqsubaddxhi,uqsubaddxhs,uqsubaddxle,uqsubaddxlo,
                uqsubaddxls,uqsubaddxlt,uqsubaddxmi,uqsubaddxne,uqsubaddxpl,
                uqsubaddxvc,uqsubaddxvs,usad8,usad8al,usad8cc,usad8cs,usad8eq,usad8ge,
                usad8gt,usad8hi,usad8hs,usad8le,usad8lo,usad8ls,usad8lt,usad8mi,
                usad8ne,usad8pl,usad8vc,usad8vs,usada8,usada8al,usada8cc,usada8cs,
                usada8eq,usada8ge,usada8gt,usada8hi,usada8hs,usada8le,usada8lo,
                usada8ls,usada8lt,usada8mi,usada8ne,usada8pl,usada8vc,usada8vs,usat,
                usat16,usat16al,usat16cc,usat16cs,usat16eq,usat16ge,usat16gt,usat16hi,
                usat16hs,usat16le,usat16lo,usat16ls,usat16lt,usat16mi,usat16ne,
                usat16pl,usat16vc,usat16vs,usatal,usatcc,usatcs,usateq,usatge,usatgt,
                usathi,usaths,usatle,usatlo,usatls,usatlt,usatmi,usatne,usatpl,usatvc,
                usatvs,usub16,usub16al,usub16cc,usub16cs,usub16eq,usub16ge,usub16gt,
                usub16hi,usub16hs,usub16le,usub16lo,usub16ls,usub16lt,usub16mi,
                usub16ne,usub16pl,usub16vc,usub16vs,usub8,usub8al,usub8cc,usub8cs,
                usub8eq,usub8ge,usub8gt,usub8hi,usub8hs,usub8le,usub8lo,usub8ls,
                usub8lt,usub8mi,usub8ne,usub8pl,usub8vc,usub8vs,usubaddx,usubaddxal,
                usubaddxcc,usubaddxcs,usubaddxeq,usubaddxge,usubaddxgt,usubaddxhi,
                usubaddxhs,usubaddxle,usubaddxlo,usubaddxls,usubaddxlt,usubaddxmi,
                usubaddxne,usubaddxpl,usubaddxvc,usubaddxvs,uxtab,uxtab16,uxtab16al,
                uxtab16cc,uxtab16cs,uxtab16eq,uxtab16ge,uxtab16gt,uxtab16hi,uxtab16hs,
                uxtab16le,uxtab16lo,uxtab16ls,uxtab16lt,uxtab16mi,uxtab16ne,uxtab16pl,
                uxtab16vc,uxtab16vs,uxtabal,uxtabcc,uxtabcs,uxtabeq,uxtabge,uxtabgt,
                uxtabhi,uxtabhs,uxtable,uxtablo,uxtabls,uxtablt,uxtabmi,uxtabne,
                uxtabpl,uxtabvc,uxtabvs,uxtah,uxtahal,uxtahcc,uxtahcs,uxtaheq,uxtahge,
                uxtahgt,uxtahhi,uxtahhs,uxtahle,uxtahlo,uxtahls,uxtahlt,uxtahmi,
                uxtahne,uxtahpl,uxtahvc,uxtahvs,uxtb,uxtb16,uxtb16al,uxtb16cc,
                uxtb16cs,uxtb16eq,uxtb16ge,uxtb16gt,uxtb16hi,uxtb16hs,uxtb16le,
                uxtb16lo,uxtb16ls,uxtb16lt,uxtb16mi,uxtb16ne,uxtb16pl,uxtb16vc,
                uxtb16vs,uxtbal,uxtbcc,uxtbcs,uxtbeq,uxtbge,uxtbgt,uxtbhi,uxtbhs,
                uxtble,uxtblo,uxtbls,uxtblt,uxtbmi,uxtbne,uxtbpl,uxtbvc,uxtbvs,uxth,
                uxthal,uxthcc,uxthcs,uxtheq,uxthge,uxthgt,uxthhi,uxthhs,uxthle,uxthlo,
                uxthls,uxthlt,uxthmi,uxthne,uxthpl,uxthvc,uxthvs,
                wfi
    """

    directives = """
                .2byte,.4byte,.8byte,.abort,.abort,.align,.altmacro,
                .arch,.arch_extension,.arm,.ascii,.asciz,.balign,.bss,
                .bundle_align_mode,.bundle_lock,,.bundle_unlock,.byte,.cantunwind,
                .cfi_endproc,,.cfi_startproc,.code,.comm,.cpu,.data,.def,.desc,.dim,
                .dn,.double,.eabi_attribute,.eject,.else,.elseif,.end,.endef,.endfunc,
                .endif,.equ,.equiv,.eqv,.err,.error,.even,.exitm,.extend,.extend.,
                .extern,.fail,.file,.fill,.float,.fnend,.fnstart,.force_thumb,.fpu,
                .func,.global,.globl,.gnu_attribute,.handlerdata,.hidden,.hword,
                .ident,.if,.incbin,.include,.inst,.inst.n,.inst.w,.int,.internal,.irp,
                .irpc,.lcomm,.ldouble,.lflags,.line,.linkonce,.list,.ln,.loc,
                .loc_mark_labels,.local,.long,.ltorg,.ltorg.,.macro,.movsp,.mri,
                .noaltmacro,.nolist,.object_arch,.octa,.offset,.org,.p2align,.packed,
                .pad,.personality,.personalityindex,.pool,.popsection,.previous,
                .print,.protected,.psize,.purgem,.pushsection,.qn,.quad,.reloc,.rept,
                .req,.save,.sbttl,.scl,.secrel32,.section,.set,.setfp,.short,.single,
                .size,.skip,.sleb128,.space,.stabd,,.stabn,,.stabs,.string,.string16,
                .string32,.string64,.string8,.struct,.subsection,.symver,.syntax,.tag,
                .text,.thumb,.thumb_func,.thumb_set,.title,.tlsdescseq,.type,.uleb128,
                .unreq,.unwind_raw,.val,.version,.vsave,.vtable_entry,.vtable_inherit,
                .warning,.weak,.weakref,.word
    """
    highlightingRules = []
    # Add highlighting rules and format for ARM assembler keywords
    keywordFormat = QtGui.QTextCharFormat()
    keywordFormat.setForeground(QtGui.QColor('darkBlue'))
    keywordFormat.setFontWeight(QtGui.QFont.Bold)
    keywordsList = keywords.replace('\n', '').replace(' ', '').split(',')
    keywordsDict = {}
    for kw in keywordsList:
        try:
            keywordsDict[kw[:3]].append(kw[3:])
        except KeyError:
            keywordsDict[kw[:3]] = [kw[3:], ]
    compactedKeywordsList = []
    for key, value in keywordsDict.items():
        compactedKeywordsList.append('{}({})'.format(key, '|'.join(value)))
    pattern = '\\b({})\\b'.format('|'.join(compactedKeywordsList))
    highlightingRules.append(HighlightingRule(QtCore.QRegExp(pattern), keywordFormat))
    # Add highlighting rules and format for ARM assembler directives
    directiveFormat = QtGui.QTextCharFormat()
    directiveFormat.setForeground(QtGui.QColor('green'))
    directiveFormat.setFontWeight(QtGui.QFont.Bold)
    pattern = '[.]({})\\b'.format('|'.join(directives.replace('\n', '').replace(' ', '').replace('.', '').split(',')))
    highlightingRules.append(HighlightingRule(QtCore.QRegExp(pattern), directiveFormat))
    # Add highlighting rules and format for ARM registers
    registerFormat = QtGui.QTextCharFormat()
    registerFormat.setForeground(QtGui.QColor('green'))
    pattern = '\\b({})\\b'.format('|'.join(['r\\d', 'r1[0-5]{0,1}', '[sS][pP]', '[lL][rR]', '[pP][cC]']))
    highlightingRules.append(HighlightingRule(QtCore.QRegExp(pattern), registerFormat))
    # Add highlighting rules and format for ARM labels
    labelFormat = QtGui.QTextCharFormat()
    labelFormat.setForeground(QtGui.QColor('black'))
    labelFormat.setFontWeight(QtGui.QFont.Bold)
    for pattern in ['^\\s*[^\\d\\s][\\w]*:', ]:
        highlightingRules.append(HighlightingRule(QtCore.QRegExp(pattern), labelFormat))
    # Add highlighting rules and format for ARM comments, tabs and spaces
    commentFormat = QtGui.QTextCharFormat()
    commentFormat.setForeground(QtGui.QColor('gray'))
    pattern = '(@.*$|^\\s*#.*$|[ \t]+)'
    highlightingRules.append(HighlightingRule(QtCore.QRegExp(pattern), commentFormat))
    return highlightingRules


class HighlightingRule:
    """A highlighting rule consists of a QRegExp pattern and its associated QTextCharFormat"""
    def __init__(self, patternTxt, hrFormat):
        self.pattern = QtCore.QRegExp(patternTxt)
        self.format = hrFormat


class ARMSyntaxHighlighter(QtGui.QSyntaxHighlighter):
    """Class that can be used to parse and highlight ARM assembler code"""

    highlightingRules = generateHighlightingRules()

    def __init__(self, parent):
        """Initializes the different patterns and their respective formats"""
        super(ARMSyntaxHighlighter, self).__init__(parent)

    def highlightBlock(self, text):
        """Parses a given block and applies the corresponding formats to the matched patterns"""
        # First, apply the patterns and formats from self.highlightingRules
        # ------------------------------------------------
        for rule in self.highlightingRules:
            index = rule.pattern.indexIn(text)
            while index >= 0:
                length = rule.pattern.matchedLength()
                self.setFormat(index, length, rule.format)
                index = rule.pattern.indexIn(text, index + length)
        # Then, deal with multiline comments
        # ------------------------------------------------
        commentStartExpression = QtCore.QRegExp('/\\*')
        commentEndExpression = QtCore.QRegExp('\\*/')
        multilineCommentFormat = QtGui.QTextCharFormat()
        multilineCommentFormat.setForeground(QtGui.QColor('gray'))
        startIndex = 0
        self.setCurrentBlockState(0)
        if self.previousBlockState() != 1:
            startIndex = commentStartExpression.indexIn(text, startIndex)
        while startIndex >= 0:
            endIndex = commentEndExpression.indexIn(text, startIndex)
            if endIndex == -1:
                self.setCurrentBlockState(1)
                commentLength = len(text) - startIndex
            else:
                commentLength = endIndex - startIndex + commentEndExpression.matchedLength()
            self.setFormat(startIndex, commentLength, multilineCommentFormat)
            startIndex = commentStartExpression.indexIn(text, startIndex + commentLength)
