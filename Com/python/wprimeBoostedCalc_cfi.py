import FWCore.ParameterSet.Config as cms

WprimeBoostedCalc = cms.PSet(
    triggerSummary = cms.InputTag("selectedPatTrigger"),
    triggerCollection = cms.InputTag("TriggerResults::HLT"),
    rhoSrc     = cms.InputTag("fixedGridRhoAll", ''),
    isWJets     = cms.bool(False),
    isTB       = cms.bool(False)
)
