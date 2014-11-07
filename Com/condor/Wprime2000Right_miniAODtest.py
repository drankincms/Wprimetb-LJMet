import FWCore.ParameterSet.Config as cms
import FWCore.PythonUtilities.LumiList as LumiList
import FWCore.ParameterSet.Types as CfgTypes

process = cms.Process("LJMetCom")

############################################################
#
# FWLite application options
process.load('LJMet.Com.ljmet_cfi')
process.ljmet.isMc = cms.bool(True)

# common calculator options
process.load('LJMet.Com.commonCalc_cfi')
process.CommonCalc.dummy_parameter = cms.string('Dummy parameter value')

# Stop calculator options
process.load('LJMet.Com.stopCalc_cfi')

# Wprime calculator options
process.load('LJMet.Com.wprimeBoostedCalc_cfi')
process.WprimeBoostedCalc.isWJets = cms.bool(False)
process.WprimeBoostedCalc.isTB = cms.bool(True)
process.WprimeBoostedCalc.isTT = cms.bool(False)

# LjetsTopoCalc options
process.load('LJMet.Com.ljetsTopoCalcNew_cfi')
process.LjetsTopoCalcNew.useBestTop = cms.bool(True)


############################################################
#
# Event selector options
#
process.event_selector = cms.PSet(

    selection = cms.string('WprimeBoostedSelector'),

    # cuts
    debug  = cms.bool(False),
    isMc  = cms.bool(True),
    
    trigger_cut  = cms.bool(True),
    dump_trigger = cms.bool(False),
    
    mctrigger_path_el = cms.string('HLT_Ele30_CaloIdVT_TrkIdT_PFNoPUJet100_PFNoPUJet25_v9'), 
    mctrigger_path_mu = cms.string('HLT_Mu40_eta2p1_v12'), 
    trigger_path_el = cms.vstring('HLT_Ele30_CaloIdVT_TrkIdT_PFNoPUJet100_PFNoPUJet25_v2','HLT_Ele30_CaloIdVT_TrkIdT_PFNoPUJet100_PFNoPUJet25_v3','HLT_Ele30_CaloIdVT_TrkIdT_PFNoPUJet100_PFNoPUJet25_v4','HLT_Ele30_CaloIdVT_TrkIdT_PFNoPUJet100_PFNoPUJet25_v5','HLT_Ele30_CaloIdVT_TrkIdT_PFNoPUJet100_PFNoPUJet25_v6','HLT_Ele30_CaloIdVT_TrkIdT_PFNoPUJet100_PFNoPUJet25_v7','HLT_Ele30_CaloIdVT_TrkIdT_PFNoPUJet100_PFNoPUJet25_v8'), 
    trigger_path_mu = cms.vstring('HLT_Mu40_eta2p1_v9','HLT_Mu40_eta2p1_v10','HLT_Mu40_eta2p1_v11'),
 
    pv_cut         = cms.bool(True),
    hbhe_cut       = cms.bool(True),
    doLaserCalFilt = cms.bool(False),

    jet_cuts                 = cms.bool(True),
    jet_minpt                = cms.double(30.0),
    jet_maxeta               = cms.double(2.4),
    min_jet                  = cms.int32(2),
    max_jet                  = cms.int32(4000),
    leading_jet_pt           = cms.double(150.0),

    muon_cuts                = cms.bool(True),
    tight_muon_minpt         = cms.double(50.0), # 26 GeV
    tight_muon_maxeta        = cms.double(2.1),
    loose_muon_minpt         = cms.double(30.0),
    loose_muon_maxeta        = cms.double(2.4),
    min_tight_muon           = cms.int32(0),

    electron_cuts                = cms.bool(True),
    tight_electron_minpt         = cms.double(50.0), # 30 GeV
    tight_electron_maxeta        = cms.double(2.5),
    loose_electron_minpt         = cms.double(30.0),
    loose_electron_maxeta        = cms.double(2.5),
    min_tight_electron           = cms.int32(0),
    
    min_tight_lepton         = cms.int32(1),
    max_tight_lepton         = cms.int32(1),
    trigger_consistent       = cms.bool(True),
    second_lepton_veto       = cms.bool(True),
    
    met_cuts                 = cms.bool(True),
    min_met                  = cms.double(20.0),
    btag_cuts                = cms.bool(False),
    
    btagger                  = cms.string('slimmedSecondaryVertices'),
    btag_min_discr           = cms.double(0.679),
    btag_1                   = cms.bool(False),
    btag_2                   = cms.bool(False),
    btag_3                   = cms.bool(False),

    BTagUncertUp             = cms.bool(False),
    BTagUncertDown           = cms.bool(False),
    JECup                    = cms.bool(False),
    JECdown                  = cms.bool(False),
    JERup                    = cms.bool(False),
    JERdown                  = cms.bool(False),
    JEC_txtfile = cms.string('../cond/Fall12_V7_DATA_UncertaintySources_AK5PFchs.txt'),
    do53xJEC                 = cms.bool(True),
    doLeptonJetCleaning      = cms.bool(True),
    
    trigger_collection       = cms.InputTag('TriggerResults::HLT'),
    pv_collection            = cms.InputTag('offlineSlimmedPrimaryVertices'),
    jet_collection           = cms.InputTag('slimmedJets'),
    muon_collection          = cms.InputTag('slimmedMuons'),
    electron_collection      = cms.InputTag('slimmedElectrons'),
    met_collection           = cms.InputTag('slimmedMETs'),
    type1corrmet_collection  = cms.InputTag('pfType1CorrectedMet'),

    )


#######################################################
#
# Input files
#
process.inputs = cms.PSet (
   nEvents    = cms.int32(20000),
    skipEvents = cms.int32(0),
    lumisToProcess = CfgTypes.untracked(CfgTypes.VLuminosityBlockRange()),
    fileNames  = cms.vstring(
		'root://cmsxrootd.fnal.gov//store/mc/Spring14miniaod/SingletopWprime_M2000GeV_right_Tune4C_13TeV-comphep/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/00000/2C794437-DF1E-E411-9467-0025901ACB64.root',
     )
)


# JSON
JsonFile = ''
myList   = LumiList.LumiList(filename=JsonFile).getCMSSWString().split(',')
if (not process.ljmet.isMc == cms.bool(True)):
    process.inputs.lumisToProcess.extend(myList)
        
#######################################################
#
# Output
#
import os
try: scratchDir=os.environ['_CONDOR_SCRATCH_DIR']
except: scratchDir='.'
if not os.path.isdir(scratchDir): os.system("mkdir -p "+scratchDir)
process.outputs = cms.PSet (
    outputName = cms.string(scratchDir+'/Wprime2000Right_miniAODtest'),
    #outputName = cms.string('Wprime2000Right_1'),
    treeName   = cms.string('ljmet'),
)

#process.outputs = cms.PSet (
#    outputName = cms.string('/uscms_data/d3/drankin/8TeV/Samples/Sep15/Wprime2000Right/Wprime2000Right_1'),
#    treeName   = cms.string('ljmet'),
#)


#######################################################
#
# Object selector options
#

# Primary vertex
process.load('PhysicsTools.SelectorUtils.pvSelector_cfi')
process.pvSelector.pvSrc   = cms.InputTag('offlineSlimmedPrimaryVertices')
process.pvSelector.minNdof = cms.double(4.0)
process.pvSelector.maxZ    = cms.double(24.0)
process.pvSelector.maxRho  = cms.double(2.0)

# Tight muon
process.load('LJMet.Com.pfMuonSelector_cfi')
process.pfMuonSelector.version = cms.string('TOPPAG12_LJETS')

# Loose muon                                                       
process.looseMuonSelector = process.pfMuonSelector.clone()
process.looseMuonSelector.version = cms.string('TOPPAG12_LJETS_MOD')


# electron
process.load('LJMet.Com.pfElectronSelector_cfi')
process.pfElectronSelector.version = cms.string('MOD')
process.pfElectronSelector.MVA = cms.double(0.9)
process.pfElectronSelector.MaxMissingHits = cms.int32(0)
process.pfElectronSelector.ConversionRejection = cms.bool(True)
process.pfElectronSelector.MinSCEta = cms.double(1.4442)
process.pfElectronSelector.MaxSCEta = cms.double(1.5660)          

# loose electron
process.loosePFElectronSelector = process.pfElectronSelector.clone()
process.loosePFElectronSelector.version = cms.string('MOD')

# jets
process.load('PhysicsTools.SelectorUtils.pfJetIDSelector_cfi') 
process.pfJetIDSelector.version = cms.string('FIRSTDATA')
process.pfJetIDSelector.quality = cms.string('LOOSE')
