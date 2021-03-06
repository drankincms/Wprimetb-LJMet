import FWCore.ParameterSet.Config as cms
import FWCore.ParameterSet.Types as CfgTypes

inputs = cms.PSet (
        nEvents    = cms.int32(1000000000000000000),
            skipEvents = cms.int32(0),
            lumisToProcess = CfgTypes.untracked(CfgTypes.VLuminosityBlockRange()),
            fileNames  = cms.vstring()
            )

inputs.fileNames.extend([
#root://xrootd.unl.edu//store/

              'dcap:///pnfs/cms/WAX/11/store/user/lpctlbsm/dsperka/SingletopWprime_M-1900_right_TuneZ2star_8TeV-comphep/Summer12_DR53X-PU_S10_START53_V7A-v1_TLBSM_53x_v2/c04f3b4fa74c8266c913b71e0c74901d/tlbsm_53x_v2_mc_8_1_DHc.root',
              'dcap:///pnfs/cms/WAX/11/store/user/lpctlbsm/dsperka/SingletopWprime_M-1900_right_TuneZ2star_8TeV-comphep/Summer12_DR53X-PU_S10_START53_V7A-v1_TLBSM_53x_v2/c04f3b4fa74c8266c913b71e0c74901d/tlbsm_53x_v2_mc_9_1_WRJ.root',
              'dcap:///pnfs/cms/WAX/11/store/user/lpctlbsm/dsperka/SingletopWprime_M-1900_right_TuneZ2star_8TeV-comphep/Summer12_DR53X-PU_S10_START53_V7A-v1_TLBSM_53x_v2/c04f3b4fa74c8266c913b71e0c74901d/tlbsm_53x_v2_mc_36_2_2su.root',
              'dcap:///pnfs/cms/WAX/11/store/user/lpctlbsm/dsperka/SingletopWprime_M-1900_right_TuneZ2star_8TeV-comphep/Summer12_DR53X-PU_S10_START53_V7A-v1_TLBSM_53x_v2/c04f3b4fa74c8266c913b71e0c74901d/tlbsm_53x_v2_mc_7_1_px8.root',
              'dcap:///pnfs/cms/WAX/11/store/user/lpctlbsm/dsperka/SingletopWprime_M-1900_right_TuneZ2star_8TeV-comphep/Summer12_DR53X-PU_S10_START53_V7A-v1_TLBSM_53x_v2/c04f3b4fa74c8266c913b71e0c74901d/tlbsm_53x_v2_mc_6_1_OlA.root',
              'dcap:///pnfs/cms/WAX/11/store/user/lpctlbsm/dsperka/SingletopWprime_M-1900_right_TuneZ2star_8TeV-comphep/Summer12_DR53X-PU_S10_START53_V7A-v1_TLBSM_53x_v2/c04f3b4fa74c8266c913b71e0c74901d/tlbsm_53x_v2_mc_5_1_w63.root',
              'dcap:///pnfs/cms/WAX/11/store/user/lpctlbsm/dsperka/SingletopWprime_M-1900_right_TuneZ2star_8TeV-comphep/Summer12_DR53X-PU_S10_START53_V7A-v1_TLBSM_53x_v2/c04f3b4fa74c8266c913b71e0c74901d/tlbsm_53x_v2_mc_56_1_2Gk.root',
              'dcap:///pnfs/cms/WAX/11/store/user/lpctlbsm/dsperka/SingletopWprime_M-1900_right_TuneZ2star_8TeV-comphep/Summer12_DR53X-PU_S10_START53_V7A-v1_TLBSM_53x_v2/c04f3b4fa74c8266c913b71e0c74901d/tlbsm_53x_v2_mc_55_1_etG.root',
              'dcap:///pnfs/cms/WAX/11/store/user/lpctlbsm/dsperka/SingletopWprime_M-1900_right_TuneZ2star_8TeV-comphep/Summer12_DR53X-PU_S10_START53_V7A-v1_TLBSM_53x_v2/c04f3b4fa74c8266c913b71e0c74901d/tlbsm_53x_v2_mc_54_1_k0w.root',
              'dcap:///pnfs/cms/WAX/11/store/user/lpctlbsm/dsperka/SingletopWprime_M-1900_right_TuneZ2star_8TeV-comphep/Summer12_DR53X-PU_S10_START53_V7A-v1_TLBSM_53x_v2/c04f3b4fa74c8266c913b71e0c74901d/tlbsm_53x_v2_mc_31_1_Rlq.root',
              'dcap:///pnfs/cms/WAX/11/store/user/lpctlbsm/dsperka/SingletopWprime_M-1900_right_TuneZ2star_8TeV-comphep/Summer12_DR53X-PU_S10_START53_V7A-v1_TLBSM_53x_v2/c04f3b4fa74c8266c913b71e0c74901d/tlbsm_53x_v2_mc_52_2_Sab.root',
              'dcap:///pnfs/cms/WAX/11/store/user/lpctlbsm/dsperka/SingletopWprime_M-1900_right_TuneZ2star_8TeV-comphep/Summer12_DR53X-PU_S10_START53_V7A-v1_TLBSM_53x_v2/c04f3b4fa74c8266c913b71e0c74901d/tlbsm_53x_v2_mc_53_1_0mS.root',
              'dcap:///pnfs/cms/WAX/11/store/user/lpctlbsm/dsperka/SingletopWprime_M-1900_right_TuneZ2star_8TeV-comphep/Summer12_DR53X-PU_S10_START53_V7A-v1_TLBSM_53x_v2/c04f3b4fa74c8266c913b71e0c74901d/tlbsm_53x_v2_mc_51_1_Gmz.root',
              'dcap:///pnfs/cms/WAX/11/store/user/lpctlbsm/dsperka/SingletopWprime_M-1900_right_TuneZ2star_8TeV-comphep/Summer12_DR53X-PU_S10_START53_V7A-v1_TLBSM_53x_v2/c04f3b4fa74c8266c913b71e0c74901d/tlbsm_53x_v2_mc_50_1_oBd.root',
              'dcap:///pnfs/cms/WAX/11/store/user/lpctlbsm/dsperka/SingletopWprime_M-1900_right_TuneZ2star_8TeV-comphep/Summer12_DR53X-PU_S10_START53_V7A-v1_TLBSM_53x_v2/c04f3b4fa74c8266c913b71e0c74901d/tlbsm_53x_v2_mc_4_1_dfU.root',
              'dcap:///pnfs/cms/WAX/11/store/user/lpctlbsm/dsperka/SingletopWprime_M-1900_right_TuneZ2star_8TeV-comphep/Summer12_DR53X-PU_S10_START53_V7A-v1_TLBSM_53x_v2/c04f3b4fa74c8266c913b71e0c74901d/tlbsm_53x_v2_mc_49_2_kJY.root',
              'dcap:///pnfs/cms/WAX/11/store/user/lpctlbsm/dsperka/SingletopWprime_M-1900_right_TuneZ2star_8TeV-comphep/Summer12_DR53X-PU_S10_START53_V7A-v1_TLBSM_53x_v2/c04f3b4fa74c8266c913b71e0c74901d/tlbsm_53x_v2_mc_28_1_Cev.root',
              'dcap:///pnfs/cms/WAX/11/store/user/lpctlbsm/dsperka/SingletopWprime_M-1900_right_TuneZ2star_8TeV-comphep/Summer12_DR53X-PU_S10_START53_V7A-v1_TLBSM_53x_v2/c04f3b4fa74c8266c913b71e0c74901d/tlbsm_53x_v2_mc_48_1_FAx.root',
              'dcap:///pnfs/cms/WAX/11/store/user/lpctlbsm/dsperka/SingletopWprime_M-1900_right_TuneZ2star_8TeV-comphep/Summer12_DR53X-PU_S10_START53_V7A-v1_TLBSM_53x_v2/c04f3b4fa74c8266c913b71e0c74901d/tlbsm_53x_v2_mc_47_2_3D4.root',
              'dcap:///pnfs/cms/WAX/11/store/user/lpctlbsm/dsperka/SingletopWprime_M-1900_right_TuneZ2star_8TeV-comphep/Summer12_DR53X-PU_S10_START53_V7A-v1_TLBSM_53x_v2/c04f3b4fa74c8266c913b71e0c74901d/tlbsm_53x_v2_mc_46_2_VTm.root',
              'dcap:///pnfs/cms/WAX/11/store/user/lpctlbsm/dsperka/SingletopWprime_M-1900_right_TuneZ2star_8TeV-comphep/Summer12_DR53X-PU_S10_START53_V7A-v1_TLBSM_53x_v2/c04f3b4fa74c8266c913b71e0c74901d/tlbsm_53x_v2_mc_45_1_3wF.root',
              'dcap:///pnfs/cms/WAX/11/store/user/lpctlbsm/dsperka/SingletopWprime_M-1900_right_TuneZ2star_8TeV-comphep/Summer12_DR53X-PU_S10_START53_V7A-v1_TLBSM_53x_v2/c04f3b4fa74c8266c913b71e0c74901d/tlbsm_53x_v2_mc_44_1_hK9.root',
              'dcap:///pnfs/cms/WAX/11/store/user/lpctlbsm/dsperka/SingletopWprime_M-1900_right_TuneZ2star_8TeV-comphep/Summer12_DR53X-PU_S10_START53_V7A-v1_TLBSM_53x_v2/c04f3b4fa74c8266c913b71e0c74901d/tlbsm_53x_v2_mc_43_1_lc4.root',
              'dcap:///pnfs/cms/WAX/11/store/user/lpctlbsm/dsperka/SingletopWprime_M-1900_right_TuneZ2star_8TeV-comphep/Summer12_DR53X-PU_S10_START53_V7A-v1_TLBSM_53x_v2/c04f3b4fa74c8266c913b71e0c74901d/tlbsm_53x_v2_mc_26_1_r2I.root',
              'dcap:///pnfs/cms/WAX/11/store/user/lpctlbsm/dsperka/SingletopWprime_M-1900_right_TuneZ2star_8TeV-comphep/Summer12_DR53X-PU_S10_START53_V7A-v1_TLBSM_53x_v2/c04f3b4fa74c8266c913b71e0c74901d/tlbsm_53x_v2_mc_42_1_e69.root',
              'dcap:///pnfs/cms/WAX/11/store/user/lpctlbsm/dsperka/SingletopWprime_M-1900_right_TuneZ2star_8TeV-comphep/Summer12_DR53X-PU_S10_START53_V7A-v1_TLBSM_53x_v2/c04f3b4fa74c8266c913b71e0c74901d/tlbsm_53x_v2_mc_41_1_Iqy.root',
              'dcap:///pnfs/cms/WAX/11/store/user/lpctlbsm/dsperka/SingletopWprime_M-1900_right_TuneZ2star_8TeV-comphep/Summer12_DR53X-PU_S10_START53_V7A-v1_TLBSM_53x_v2/c04f3b4fa74c8266c913b71e0c74901d/tlbsm_53x_v2_mc_40_2_39j.root',
              'dcap:///pnfs/cms/WAX/11/store/user/lpctlbsm/dsperka/SingletopWprime_M-1900_right_TuneZ2star_8TeV-comphep/Summer12_DR53X-PU_S10_START53_V7A-v1_TLBSM_53x_v2/c04f3b4fa74c8266c913b71e0c74901d/tlbsm_53x_v2_mc_3_1_nRJ.root',
              'dcap:///pnfs/cms/WAX/11/store/user/lpctlbsm/dsperka/SingletopWprime_M-1900_right_TuneZ2star_8TeV-comphep/Summer12_DR53X-PU_S10_START53_V7A-v1_TLBSM_53x_v2/c04f3b4fa74c8266c913b71e0c74901d/tlbsm_53x_v2_mc_39_1_ocD.root',
              'dcap:///pnfs/cms/WAX/11/store/user/lpctlbsm/dsperka/SingletopWprime_M-1900_right_TuneZ2star_8TeV-comphep/Summer12_DR53X-PU_S10_START53_V7A-v1_TLBSM_53x_v2/c04f3b4fa74c8266c913b71e0c74901d/tlbsm_53x_v2_mc_38_2_2MV.root',
              'dcap:///pnfs/cms/WAX/11/store/user/lpctlbsm/dsperka/SingletopWprime_M-1900_right_TuneZ2star_8TeV-comphep/Summer12_DR53X-PU_S10_START53_V7A-v1_TLBSM_53x_v2/c04f3b4fa74c8266c913b71e0c74901d/tlbsm_53x_v2_mc_37_2_Esy.root',
              'dcap:///pnfs/cms/WAX/11/store/user/lpctlbsm/dsperka/SingletopWprime_M-1900_right_TuneZ2star_8TeV-comphep/Summer12_DR53X-PU_S10_START53_V7A-v1_TLBSM_53x_v2/c04f3b4fa74c8266c913b71e0c74901d/tlbsm_53x_v2_mc_35_2_LkP.root',
              'dcap:///pnfs/cms/WAX/11/store/user/lpctlbsm/dsperka/SingletopWprime_M-1900_right_TuneZ2star_8TeV-comphep/Summer12_DR53X-PU_S10_START53_V7A-v1_TLBSM_53x_v2/c04f3b4fa74c8266c913b71e0c74901d/tlbsm_53x_v2_mc_34_2_2xS.root',
              'dcap:///pnfs/cms/WAX/11/store/user/lpctlbsm/dsperka/SingletopWprime_M-1900_right_TuneZ2star_8TeV-comphep/Summer12_DR53X-PU_S10_START53_V7A-v1_TLBSM_53x_v2/c04f3b4fa74c8266c913b71e0c74901d/tlbsm_53x_v2_mc_20_1_Mm7.root',
              'dcap:///pnfs/cms/WAX/11/store/user/lpctlbsm/dsperka/SingletopWprime_M-1900_right_TuneZ2star_8TeV-comphep/Summer12_DR53X-PU_S10_START53_V7A-v1_TLBSM_53x_v2/c04f3b4fa74c8266c913b71e0c74901d/tlbsm_53x_v2_mc_33_1_krS.root',
              'dcap:///pnfs/cms/WAX/11/store/user/lpctlbsm/dsperka/SingletopWprime_M-1900_right_TuneZ2star_8TeV-comphep/Summer12_DR53X-PU_S10_START53_V7A-v1_TLBSM_53x_v2/c04f3b4fa74c8266c913b71e0c74901d/tlbsm_53x_v2_mc_32_1_v1Z.root',
              'dcap:///pnfs/cms/WAX/11/store/user/lpctlbsm/dsperka/SingletopWprime_M-1900_right_TuneZ2star_8TeV-comphep/Summer12_DR53X-PU_S10_START53_V7A-v1_TLBSM_53x_v2/c04f3b4fa74c8266c913b71e0c74901d/tlbsm_53x_v2_mc_30_1_ZnA.root',
              'dcap:///pnfs/cms/WAX/11/store/user/lpctlbsm/dsperka/SingletopWprime_M-1900_right_TuneZ2star_8TeV-comphep/Summer12_DR53X-PU_S10_START53_V7A-v1_TLBSM_53x_v2/c04f3b4fa74c8266c913b71e0c74901d/tlbsm_53x_v2_mc_2_1_LNA.root',
              'dcap:///pnfs/cms/WAX/11/store/user/lpctlbsm/dsperka/SingletopWprime_M-1900_right_TuneZ2star_8TeV-comphep/Summer12_DR53X-PU_S10_START53_V7A-v1_TLBSM_53x_v2/c04f3b4fa74c8266c913b71e0c74901d/tlbsm_53x_v2_mc_29_1_kRy.root',
              'dcap:///pnfs/cms/WAX/11/store/user/lpctlbsm/dsperka/SingletopWprime_M-1900_right_TuneZ2star_8TeV-comphep/Summer12_DR53X-PU_S10_START53_V7A-v1_TLBSM_53x_v2/c04f3b4fa74c8266c913b71e0c74901d/tlbsm_53x_v2_mc_19_1_PIi.root',
              'dcap:///pnfs/cms/WAX/11/store/user/lpctlbsm/dsperka/SingletopWprime_M-1900_right_TuneZ2star_8TeV-comphep/Summer12_DR53X-PU_S10_START53_V7A-v1_TLBSM_53x_v2/c04f3b4fa74c8266c913b71e0c74901d/tlbsm_53x_v2_mc_27_1_Jua.root',
              'dcap:///pnfs/cms/WAX/11/store/user/lpctlbsm/dsperka/SingletopWprime_M-1900_right_TuneZ2star_8TeV-comphep/Summer12_DR53X-PU_S10_START53_V7A-v1_TLBSM_53x_v2/c04f3b4fa74c8266c913b71e0c74901d/tlbsm_53x_v2_mc_25_1_r1S.root',
              'dcap:///pnfs/cms/WAX/11/store/user/lpctlbsm/dsperka/SingletopWprime_M-1900_right_TuneZ2star_8TeV-comphep/Summer12_DR53X-PU_S10_START53_V7A-v1_TLBSM_53x_v2/c04f3b4fa74c8266c913b71e0c74901d/tlbsm_53x_v2_mc_24_1_CaE.root',
              'dcap:///pnfs/cms/WAX/11/store/user/lpctlbsm/dsperka/SingletopWprime_M-1900_right_TuneZ2star_8TeV-comphep/Summer12_DR53X-PU_S10_START53_V7A-v1_TLBSM_53x_v2/c04f3b4fa74c8266c913b71e0c74901d/tlbsm_53x_v2_mc_23_1_L8d.root',
              'dcap:///pnfs/cms/WAX/11/store/user/lpctlbsm/dsperka/SingletopWprime_M-1900_right_TuneZ2star_8TeV-comphep/Summer12_DR53X-PU_S10_START53_V7A-v1_TLBSM_53x_v2/c04f3b4fa74c8266c913b71e0c74901d/tlbsm_53x_v2_mc_22_1_5RP.root',
              'dcap:///pnfs/cms/WAX/11/store/user/lpctlbsm/dsperka/SingletopWprime_M-1900_right_TuneZ2star_8TeV-comphep/Summer12_DR53X-PU_S10_START53_V7A-v1_TLBSM_53x_v2/c04f3b4fa74c8266c913b71e0c74901d/tlbsm_53x_v2_mc_21_1_VVi.root',
              'dcap:///pnfs/cms/WAX/11/store/user/lpctlbsm/dsperka/SingletopWprime_M-1900_right_TuneZ2star_8TeV-comphep/Summer12_DR53X-PU_S10_START53_V7A-v1_TLBSM_53x_v2/c04f3b4fa74c8266c913b71e0c74901d/tlbsm_53x_v2_mc_1_1_DWD.root',
              'dcap:///pnfs/cms/WAX/11/store/user/lpctlbsm/dsperka/SingletopWprime_M-1900_right_TuneZ2star_8TeV-comphep/Summer12_DR53X-PU_S10_START53_V7A-v1_TLBSM_53x_v2/c04f3b4fa74c8266c913b71e0c74901d/tlbsm_53x_v2_mc_18_1_MlP.root',
              'dcap:///pnfs/cms/WAX/11/store/user/lpctlbsm/dsperka/SingletopWprime_M-1900_right_TuneZ2star_8TeV-comphep/Summer12_DR53X-PU_S10_START53_V7A-v1_TLBSM_53x_v2/c04f3b4fa74c8266c913b71e0c74901d/tlbsm_53x_v2_mc_17_1_q7e.root',
              'dcap:///pnfs/cms/WAX/11/store/user/lpctlbsm/dsperka/SingletopWprime_M-1900_right_TuneZ2star_8TeV-comphep/Summer12_DR53X-PU_S10_START53_V7A-v1_TLBSM_53x_v2/c04f3b4fa74c8266c913b71e0c74901d/tlbsm_53x_v2_mc_16_1_mIM.root',
              'dcap:///pnfs/cms/WAX/11/store/user/lpctlbsm/dsperka/SingletopWprime_M-1900_right_TuneZ2star_8TeV-comphep/Summer12_DR53X-PU_S10_START53_V7A-v1_TLBSM_53x_v2/c04f3b4fa74c8266c913b71e0c74901d/tlbsm_53x_v2_mc_15_1_vFu.root',
              'dcap:///pnfs/cms/WAX/11/store/user/lpctlbsm/dsperka/SingletopWprime_M-1900_right_TuneZ2star_8TeV-comphep/Summer12_DR53X-PU_S10_START53_V7A-v1_TLBSM_53x_v2/c04f3b4fa74c8266c913b71e0c74901d/tlbsm_53x_v2_mc_14_1_QPL.root',
              'dcap:///pnfs/cms/WAX/11/store/user/lpctlbsm/dsperka/SingletopWprime_M-1900_right_TuneZ2star_8TeV-comphep/Summer12_DR53X-PU_S10_START53_V7A-v1_TLBSM_53x_v2/c04f3b4fa74c8266c913b71e0c74901d/tlbsm_53x_v2_mc_12_1_waZ.root',
              'dcap:///pnfs/cms/WAX/11/store/user/lpctlbsm/dsperka/SingletopWprime_M-1900_right_TuneZ2star_8TeV-comphep/Summer12_DR53X-PU_S10_START53_V7A-v1_TLBSM_53x_v2/c04f3b4fa74c8266c913b71e0c74901d/tlbsm_53x_v2_mc_13_1_Zkq.root',
              'dcap:///pnfs/cms/WAX/11/store/user/lpctlbsm/dsperka/SingletopWprime_M-1900_right_TuneZ2star_8TeV-comphep/Summer12_DR53X-PU_S10_START53_V7A-v1_TLBSM_53x_v2/c04f3b4fa74c8266c913b71e0c74901d/tlbsm_53x_v2_mc_11_1_ZOZ.root',
              'dcap:///pnfs/cms/WAX/11/store/user/lpctlbsm/dsperka/SingletopWprime_M-1900_right_TuneZ2star_8TeV-comphep/Summer12_DR53X-PU_S10_START53_V7A-v1_TLBSM_53x_v2/c04f3b4fa74c8266c913b71e0c74901d/tlbsm_53x_v2_mc_10_1_sDc.root'

            ])
