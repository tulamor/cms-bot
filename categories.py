# A ridicously long mapping for categories. Good enough for now.
from cms_static import GH_CMSDIST_REPO as gh_cmsdist
from cms_static import GH_CMSSW_ORGANIZATION as gh_user
from cms_static import GH_CMSSW_REPO as gh_cmssw
from categories_map import CMSSW_CATEGORIES
from repo_config import CMSBUILD_USER
from releases import SPECIAL_RELEASE_MANAGERS

authors = {}
GITHUB_BLACKLIST_AUTHORS = []
CMSSW_L1 = ["dpiparo", "silviodonato"]
APPROVE_BUILD_RELEASE =  list(set([ "smuzaffar"] + CMSSW_L1 + SPECIAL_RELEASE_MANAGERS))
REQUEST_BUILD_RELEASE = APPROVE_BUILD_RELEASE
TRIGGER_PR_TESTS = list(set([ "felicepantaleo", "rovere", "lgray", "bsunanda", "VinInn", "kpedro88", "makortel", "wddgit", "mtosi", "gpetruc", "gartung", "nsmith-","mmusich"] + REQUEST_BUILD_RELEASE + [ a for a in authors if authors[a]>10 and not a in GITHUB_BLACKLIST_AUTHORS ]))
PR_HOLD_MANAGERS = [ "kpedro88" ]

COMMON_CATEGORIES = [ "orp", "tests", "code-checks" ]
EXTERNAL_CATEGORIES = [ "externals" ]
EXTERNAL_REPOS = [ "cms-data", "cms-externals", gh_user]

CMSSW_REPOS = [ gh_user+"/"+gh_cmssw ]
CMSDIST_REPOS = [ gh_user+"/"+gh_cmsdist ]
CMSSW_ISSUES_TRACKERS = list(set(CMSSW_L1 + [ "smuzaffar", "Dr15Jones", "makortel" ]))
COMPARISON_MISSING_MAP = [ "slava77" ]

CMSSW_L2 = {
  "Dr15Jones":        ["core", "visualization", "geometry"],
  "Martin-Grunewald": ["hlt"],
  "alberto-sanchez":  ["generators"],
  "agrohsje":         ["generators"],
  "alja":             ["visualization"],
  "andrius-k":        ["dqm"],
  "benkrikler":       ["l1"],
  "chayanit":         ["pdmv"],
  "civanch":          ["simulation", "geometry", "fastsim"],
  "cmsdoxy":          ["docs"],
  "cvuosalo":         ["geometry"],
  "davidlange6":      ["operations"],
  "emeschi":          ["daq"],
  "fabiocos":         ["operations"],
  "fgolf":            ["xpog"],
  "franzoni":         ["operations"],
  "fwyzard":          ["heterogeneous", "hlt"],
  "ggovi":            ["db"],
  "GurpreetSinghChahal":  ["generators"],
  "ianna":            ["geometry"],
  "jfernan2":         ["dqm"],
  "kmaeshima":        ["dqm"],
  "fioriNTU":         ["dqm"],
  "kpedro88":         ["upgrade"],
  "lveldere":         ["fastsim"],
  "makortel":         ["heterogeneous", "core", "visualization", "geometry"],
  "mdhildreth":       ["simulation", "geometry", "fastsim"],
  "mkirsano":         ["generators"],   
  "mommsen":          ["daq"],
  "mrodozov":         ["externals"],
  "perrotta":         ["reconstruction"],
  "peruzzim":         ["xpog"],
  "pgunnell":         ["pdmv"],
  "pohsun":           ["alca"],
  "qliphy":           ["generators"],
  "rekovic":          ["l1"],
  "santocch":         ["analysis"],
  "sbein":            ["fastsim"],
  "schneiml":         ["dqm"],
  "SiewYan":          ["generators"], 
  "silviodonato":     ["operations"],
  "slava77":          ["reconstruction"],
  "smuzaffar":        ["core", "externals"],
  "tulamor":          ["externals"],
  "ssekmen":          ["fastsim"],
  "tlampen":          ["alca"],
  "tocheng":          ["alca"],
  "wajidalikhan":     ["pdmv"],
  "christopheralanwest": ["alca"],
  CMSBUILD_USER:      ["tests" ],
}

USERS_TO_TRIGGER_HOOKS = set(TRIGGER_PR_TESTS + CMSSW_ISSUES_TRACKERS + list(CMSSW_L2.keys()))
CMS_REPOS = set(CMSDIST_REPOS + CMSSW_REPOS + EXTERNAL_REPOS)
from datetime import datetime
COMMENT_CONVERSION = {}
COMMENT_CONVERSION['kpedro88']={'comments_before': datetime.strptime('2018-07-13','%Y-%m-%d'), 'comments':[('+1', '+upgrade')]}


def external_to_package(repo_fullname):
  org, repo = repo_fullname.split("/",1)
  if org == "cms-data":
    return repo.replace('-','/')
  return ''
