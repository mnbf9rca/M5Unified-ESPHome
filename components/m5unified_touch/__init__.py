import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import touchscreen
from esphome.const import CONF_ID

DEPENDENCIES = ["m5unified"]

m5unified_touch_ns = cg.esphome_ns.namespace("m5unified_touch")
M5UnifiedTouch = m5unified_touch_ns.class_("M5UnifiedTouch", touchscreen.Touchscreen)

CONFIG_SCHEMA = touchscreen.TOUCHSCREEN_SCHEMA.extend({
    cv.GenerateID(): cv.declare_id(M5UnifiedTouch),
}).extend(cv.COMPONENT_SCHEMA)

async def to_code(config):
    var = await touchscreen.register_touchscreen(config)
    await cg.register_component(var, config)