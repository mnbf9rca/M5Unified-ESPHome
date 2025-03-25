import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import touchscreen
from esphome.const import CONF_ID
import logging

_LOGGER = logging.getLogger(__name__)
_LOGGER.setLevel(logging.DEBUG)

DEPENDENCIES = ['m5unified_touch']

_LOGGER.debug("=== Initializing m5unified_touch platform ===")

# Import the M5UnifiedTouch class from our base component
m5unified_touch_ns = cg.esphome_ns.namespace('m5unified_touch')
M5UnifiedTouch = m5unified_touch_ns.class_('M5UnifiedTouch', touchscreen.Touchscreen)

async def to_code(config):
    _LOGGER.debug(f"Platform to_code called with config: {config}")
    var = cg.new_Pvariable(config[CONF_ID])
    await touchscreen.register_touchscreen(var, config)
    await cg.register_component(var, config)
    return var

# Define the platform configuration schema
CONFIG_SCHEMA = touchscreen.TOUCHSCREEN_SCHEMA.extend({
    cv.GenerateID(): cv.declare_id(M5UnifiedTouch)
}).extend(cv.COMPONENT_SCHEMA)