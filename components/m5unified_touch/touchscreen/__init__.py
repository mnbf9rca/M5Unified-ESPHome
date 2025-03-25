import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import touchscreen
from esphome.const import CONF_ID

DEPENDENCIES = ["m5unified_touch"]
AUTO_LOAD = ["touchscreen"]

m5unified_touch_ns = cg.esphome_ns.namespace("esphome::m5unified_touch")
M5UnifiedTouchPlatform = m5unified_touch_ns.class_("M5UnifiedTouchPlatform", touchscreen.Touchscreen)

CONFIG_SCHEMA = touchscreen.TOUCHSCREEN_SCHEMA.extend({
    cv.GenerateID(): cv.declare_id(M5UnifiedTouchPlatform),
})

async def to_code(config):
    var = await cg.get_variable(config[CONF_ID])
    await touchscreen.setup_touchscreen(var, config)