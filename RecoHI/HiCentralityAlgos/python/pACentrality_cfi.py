import FWCore.ParameterSet.Config as cms

pACentrality = cms.EDProducer("CentralityProducer",

                            produceHFhits = cms.bool(True),
                            produceHFtowers = cms.bool(True),
                            produceEcalhits = cms.bool(True),
                            produceZDChits = cms.bool(True),
                            produceETmidRapidity = cms.bool(True),
                            producePixelhits = cms.bool(True),
                            produceTracks = cms.bool(True),
                            producePixelTracks = cms.bool(True),
                            producePF = cms.bool(True),
                            reUseCentrality = cms.bool(False),
                            
                            srcHFhits = cms.InputTag("hfreco"),
                            srcTowers = cms.InputTag("towerMaker"),
                            srcEBhits = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
                            srcEEhits = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
                            srcZDChits = cms.InputTag("zdcreco"),
                            srcPixelhits = cms.InputTag("siPixelRecHits"),
                            srcTracks = cms.InputTag("generalTracks"),
                            srcVertex= cms.InputTag("offlinePrimaryVertices"),
                            srcReUse = cms.InputTag("pACentrality"),
                            srcPixelTracks = cms.InputTag("pixelTracks"),
                            srcPF = cms.InputTag("particleFlow"),

                            doPixelCut = cms.bool(True),
                            useQuality = cms.bool(True),
                            trackQuality = cms.string('highPurity'),
                            trackEtaCut = cms.double(2),
                            trackPtCut = cms.double(1),
                            hfEtaCut = cms.double(4), #hf above the absolute value of this cut is used
                            midRapidityRange = cms.double(1),
			    lowGainZDC = cms.bool(True),

                            )

from Configuration.Eras.Modifier_run3_common_cff import run3_common
run3_common.toModify(pACentrality, srcZDChits = "zdcrecoRun3",lowGainZDC =False)

