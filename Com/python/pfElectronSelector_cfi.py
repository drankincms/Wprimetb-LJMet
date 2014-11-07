import FWCore.ParameterSet.Config as cms

#Electron Selector
pfElectronSelector = cms.PSet(
    version = cms.string('SPRING11'),
    MVA = cms.double(0.9),
    MaxMissingHits = cms.int32(0),
    D0 = cms.double(0.02),
    DZ = cms.double(0.5),
    electronIDused = cms.string('eidTight'),
    ConversionRejection = cms.bool(True),
    PFIso = cms.double(0.1),
    MinSCEta = cms.double(1.4442),
    MaxSCEta = cms.double(1.5660),
    cutsToIgnore = cms.vstring()
    )


