import FWCore.ParameterSet.Config as cms

def PATInput() : 
    readFiles = cms.untracked.vstring()
    readFiles.extend( [
	'dcap:///pnfs/fnal.gov/usr/cms/WAX/11/store/user/kukartse/Rutgers_WbG_150GeV_v1_Fastsim-AODSIM/TLBSM_v1-PAT/ttbsm_42x_mc_1_1_QtB.root',
	'dcap:///pnfs/fnal.gov/usr/cms/WAX/11/store/user/kukartse/Rutgers_WbG_150GeV_v1_Fastsim-AODSIM/TLBSM_v1-PAT/ttbsm_42x_mc_10_1_HmD.root',
	'dcap:///pnfs/fnal.gov/usr/cms/WAX/11/store/user/kukartse/Rutgers_WbG_150GeV_v1_Fastsim-AODSIM/TLBSM_v1-PAT/ttbsm_42x_mc_11_1_MWO.root',
	'dcap:///pnfs/fnal.gov/usr/cms/WAX/11/store/user/kukartse/Rutgers_WbG_150GeV_v1_Fastsim-AODSIM/TLBSM_v1-PAT/ttbsm_42x_mc_12_1_fFk.root',
	'dcap:///pnfs/fnal.gov/usr/cms/WAX/11/store/user/kukartse/Rutgers_WbG_150GeV_v1_Fastsim-AODSIM/TLBSM_v1-PAT/ttbsm_42x_mc_13_1_WFX.root',
	'dcap:///pnfs/fnal.gov/usr/cms/WAX/11/store/user/kukartse/Rutgers_WbG_150GeV_v1_Fastsim-AODSIM/TLBSM_v1-PAT/ttbsm_42x_mc_14_1_KFH.root',
	'dcap:///pnfs/fnal.gov/usr/cms/WAX/11/store/user/kukartse/Rutgers_WbG_150GeV_v1_Fastsim-AODSIM/TLBSM_v1-PAT/ttbsm_42x_mc_15_1_KPl.root',
	'dcap:///pnfs/fnal.gov/usr/cms/WAX/11/store/user/kukartse/Rutgers_WbG_150GeV_v1_Fastsim-AODSIM/TLBSM_v1-PAT/ttbsm_42x_mc_16_1_vqo.root',
	'dcap:///pnfs/fnal.gov/usr/cms/WAX/11/store/user/kukartse/Rutgers_WbG_150GeV_v1_Fastsim-AODSIM/TLBSM_v1-PAT/ttbsm_42x_mc_17_1_TNj.root',
	'dcap:///pnfs/fnal.gov/usr/cms/WAX/11/store/user/kukartse/Rutgers_WbG_150GeV_v1_Fastsim-AODSIM/TLBSM_v1-PAT/ttbsm_42x_mc_18_1_l3V.root',
	'dcap:///pnfs/fnal.gov/usr/cms/WAX/11/store/user/kukartse/Rutgers_WbG_150GeV_v1_Fastsim-AODSIM/TLBSM_v1-PAT/ttbsm_42x_mc_19_1_tzV.root',
	'dcap:///pnfs/fnal.gov/usr/cms/WAX/11/store/user/kukartse/Rutgers_WbG_150GeV_v1_Fastsim-AODSIM/TLBSM_v1-PAT/ttbsm_42x_mc_2_1_qDI.root',
	'dcap:///pnfs/fnal.gov/usr/cms/WAX/11/store/user/kukartse/Rutgers_WbG_150GeV_v1_Fastsim-AODSIM/TLBSM_v1-PAT/ttbsm_42x_mc_20_1_5yB.root',
	'dcap:///pnfs/fnal.gov/usr/cms/WAX/11/store/user/kukartse/Rutgers_WbG_150GeV_v1_Fastsim-AODSIM/TLBSM_v1-PAT/ttbsm_42x_mc_21_1_KuH.root',
	'dcap:///pnfs/fnal.gov/usr/cms/WAX/11/store/user/kukartse/Rutgers_WbG_150GeV_v1_Fastsim-AODSIM/TLBSM_v1-PAT/ttbsm_42x_mc_22_1_RqM.root',
	'dcap:///pnfs/fnal.gov/usr/cms/WAX/11/store/user/kukartse/Rutgers_WbG_150GeV_v1_Fastsim-AODSIM/TLBSM_v1-PAT/ttbsm_42x_mc_23_1_rUk.root',
	'dcap:///pnfs/fnal.gov/usr/cms/WAX/11/store/user/kukartse/Rutgers_WbG_150GeV_v1_Fastsim-AODSIM/TLBSM_v1-PAT/ttbsm_42x_mc_24_1_adI.root',
	'dcap:///pnfs/fnal.gov/usr/cms/WAX/11/store/user/kukartse/Rutgers_WbG_150GeV_v1_Fastsim-AODSIM/TLBSM_v1-PAT/ttbsm_42x_mc_25_1_ACK.root',
	'dcap:///pnfs/fnal.gov/usr/cms/WAX/11/store/user/kukartse/Rutgers_WbG_150GeV_v1_Fastsim-AODSIM/TLBSM_v1-PAT/ttbsm_42x_mc_26_2_2fv.root',
	'dcap:///pnfs/fnal.gov/usr/cms/WAX/11/store/user/kukartse/Rutgers_WbG_150GeV_v1_Fastsim-AODSIM/TLBSM_v1-PAT/ttbsm_42x_mc_27_2_QtK.root',
	'dcap:///pnfs/fnal.gov/usr/cms/WAX/11/store/user/kukartse/Rutgers_WbG_150GeV_v1_Fastsim-AODSIM/TLBSM_v1-PAT/ttbsm_42x_mc_28_1_Liu.root',
	'dcap:///pnfs/fnal.gov/usr/cms/WAX/11/store/user/kukartse/Rutgers_WbG_150GeV_v1_Fastsim-AODSIM/TLBSM_v1-PAT/ttbsm_42x_mc_29_1_42E.root',
	'dcap:///pnfs/fnal.gov/usr/cms/WAX/11/store/user/kukartse/Rutgers_WbG_150GeV_v1_Fastsim-AODSIM/TLBSM_v1-PAT/ttbsm_42x_mc_3_1_JUO.root',
	'dcap:///pnfs/fnal.gov/usr/cms/WAX/11/store/user/kukartse/Rutgers_WbG_150GeV_v1_Fastsim-AODSIM/TLBSM_v1-PAT/ttbsm_42x_mc_30_1_Wur.root',
	'dcap:///pnfs/fnal.gov/usr/cms/WAX/11/store/user/kukartse/Rutgers_WbG_150GeV_v1_Fastsim-AODSIM/TLBSM_v1-PAT/ttbsm_42x_mc_31_1_bmv.root',
	'dcap:///pnfs/fnal.gov/usr/cms/WAX/11/store/user/kukartse/Rutgers_WbG_150GeV_v1_Fastsim-AODSIM/TLBSM_v1-PAT/ttbsm_42x_mc_32_1_zrn.root',
	'dcap:///pnfs/fnal.gov/usr/cms/WAX/11/store/user/kukartse/Rutgers_WbG_150GeV_v1_Fastsim-AODSIM/TLBSM_v1-PAT/ttbsm_42x_mc_33_1_HxO.root',
	'dcap:///pnfs/fnal.gov/usr/cms/WAX/11/store/user/kukartse/Rutgers_WbG_150GeV_v1_Fastsim-AODSIM/TLBSM_v1-PAT/ttbsm_42x_mc_34_1_ppr.root',
	'dcap:///pnfs/fnal.gov/usr/cms/WAX/11/store/user/kukartse/Rutgers_WbG_150GeV_v1_Fastsim-AODSIM/TLBSM_v1-PAT/ttbsm_42x_mc_35_1_jiO.root',
	'dcap:///pnfs/fnal.gov/usr/cms/WAX/11/store/user/kukartse/Rutgers_WbG_150GeV_v1_Fastsim-AODSIM/TLBSM_v1-PAT/ttbsm_42x_mc_36_1_oMR.root',
	'dcap:///pnfs/fnal.gov/usr/cms/WAX/11/store/user/kukartse/Rutgers_WbG_150GeV_v1_Fastsim-AODSIM/TLBSM_v1-PAT/ttbsm_42x_mc_37_1_t2G.root',
	'dcap:///pnfs/fnal.gov/usr/cms/WAX/11/store/user/kukartse/Rutgers_WbG_150GeV_v1_Fastsim-AODSIM/TLBSM_v1-PAT/ttbsm_42x_mc_38_1_wwA.root',
	'dcap:///pnfs/fnal.gov/usr/cms/WAX/11/store/user/kukartse/Rutgers_WbG_150GeV_v1_Fastsim-AODSIM/TLBSM_v1-PAT/ttbsm_42x_mc_39_1_5Ex.root',
	'dcap:///pnfs/fnal.gov/usr/cms/WAX/11/store/user/kukartse/Rutgers_WbG_150GeV_v1_Fastsim-AODSIM/TLBSM_v1-PAT/ttbsm_42x_mc_4_1_B6W.root',
	'dcap:///pnfs/fnal.gov/usr/cms/WAX/11/store/user/kukartse/Rutgers_WbG_150GeV_v1_Fastsim-AODSIM/TLBSM_v1-PAT/ttbsm_42x_mc_40_1_H3N.root',
	'dcap:///pnfs/fnal.gov/usr/cms/WAX/11/store/user/kukartse/Rutgers_WbG_150GeV_v1_Fastsim-AODSIM/TLBSM_v1-PAT/ttbsm_42x_mc_41_1_FAA.root',
	'dcap:///pnfs/fnal.gov/usr/cms/WAX/11/store/user/kukartse/Rutgers_WbG_150GeV_v1_Fastsim-AODSIM/TLBSM_v1-PAT/ttbsm_42x_mc_42_1_fwY.root',
	'dcap:///pnfs/fnal.gov/usr/cms/WAX/11/store/user/kukartse/Rutgers_WbG_150GeV_v1_Fastsim-AODSIM/TLBSM_v1-PAT/ttbsm_42x_mc_43_1_08O.root',
	'dcap:///pnfs/fnal.gov/usr/cms/WAX/11/store/user/kukartse/Rutgers_WbG_150GeV_v1_Fastsim-AODSIM/TLBSM_v1-PAT/ttbsm_42x_mc_44_1_RBB.root',
	'dcap:///pnfs/fnal.gov/usr/cms/WAX/11/store/user/kukartse/Rutgers_WbG_150GeV_v1_Fastsim-AODSIM/TLBSM_v1-PAT/ttbsm_42x_mc_45_1_njO.root',
	'dcap:///pnfs/fnal.gov/usr/cms/WAX/11/store/user/kukartse/Rutgers_WbG_150GeV_v1_Fastsim-AODSIM/TLBSM_v1-PAT/ttbsm_42x_mc_46_1_dg5.root',
	'dcap:///pnfs/fnal.gov/usr/cms/WAX/11/store/user/kukartse/Rutgers_WbG_150GeV_v1_Fastsim-AODSIM/TLBSM_v1-PAT/ttbsm_42x_mc_47_1_6Z8.root',
	'dcap:///pnfs/fnal.gov/usr/cms/WAX/11/store/user/kukartse/Rutgers_WbG_150GeV_v1_Fastsim-AODSIM/TLBSM_v1-PAT/ttbsm_42x_mc_48_1_TS0.root',
	'dcap:///pnfs/fnal.gov/usr/cms/WAX/11/store/user/kukartse/Rutgers_WbG_150GeV_v1_Fastsim-AODSIM/TLBSM_v1-PAT/ttbsm_42x_mc_49_1_wwK.root',
	'dcap:///pnfs/fnal.gov/usr/cms/WAX/11/store/user/kukartse/Rutgers_WbG_150GeV_v1_Fastsim-AODSIM/TLBSM_v1-PAT/ttbsm_42x_mc_5_1_oFz.root',
	'dcap:///pnfs/fnal.gov/usr/cms/WAX/11/store/user/kukartse/Rutgers_WbG_150GeV_v1_Fastsim-AODSIM/TLBSM_v1-PAT/ttbsm_42x_mc_50_1_FoU.root',
	'dcap:///pnfs/fnal.gov/usr/cms/WAX/11/store/user/kukartse/Rutgers_WbG_150GeV_v1_Fastsim-AODSIM/TLBSM_v1-PAT/ttbsm_42x_mc_6_1_TIw.root',
	'dcap:///pnfs/fnal.gov/usr/cms/WAX/11/store/user/kukartse/Rutgers_WbG_150GeV_v1_Fastsim-AODSIM/TLBSM_v1-PAT/ttbsm_42x_mc_7_1_guo.root',
	'dcap:///pnfs/fnal.gov/usr/cms/WAX/11/store/user/kukartse/Rutgers_WbG_150GeV_v1_Fastsim-AODSIM/TLBSM_v1-PAT/ttbsm_42x_mc_8_1_tji.root',
	'dcap:///pnfs/fnal.gov/usr/cms/WAX/11/store/user/kukartse/Rutgers_WbG_150GeV_v1_Fastsim-AODSIM/TLBSM_v1-PAT/ttbsm_42x_mc_9_1_VRl.root',
	'dcap:///pnfs/fnal.gov/usr/cms/WAX/11/store/user/kukartse/Rutgers_WbG_150GeV_v1_Fastsim-AODSIM/TLBSM_v1-PAT/ttbsm_42x_mc_26_2_2fv.root',
	'dcap:///pnfs/fnal.gov/usr/cms/WAX/11/store/user/kukartse/Rutgers_WbG_150GeV_v1_Fastsim-AODSIM/TLBSM_v1-PAT/ttbsm_42x_mc_27_2_QtK.root' ] )

    return cms.Source("PoolSource",
                      debugVerbosity = cms.untracked.uint32(200),
                      debugFlag = cms.untracked.bool(True),
                      fileNames = readFiles
                      )
#
# The original number of events: 0
# Number of passed events: 0
