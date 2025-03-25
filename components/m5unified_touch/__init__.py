"""M5Unified touch component."""
import esphome.codegen as cg
import esphome.config_validation as cv

CODEOWNERS = ["@mnbf9rca"]
DEPENDENCIES = ["m5unified"]

m5unified_touch_ns = cg.esphome_ns.namespace("esphome::m5unified_touch")