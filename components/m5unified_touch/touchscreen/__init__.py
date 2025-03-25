import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import touchscreen
from esphome.const import CONF_ID

DEPENDENCIES = ["m5unified_touch"]
AUTO_LOAD = ["touchscreen"]

# Import the base component
from . import M5UnifiedTouch

CONFIG_SCHEMA = touchscreen.TOUCHSCREEN_SCHEMA.extend({
    cv.GenerateID(): cv.declare_id(M5UnifiedTouch),
})

async def to_code(config):
    var = await cg.get_variable(config[CONF_ID])
    await touchscreen.setup_touchscreen(var, config)