import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import touchscreen
from esphome.const import CONF_ID
import logging

_LOGGER = logging.getLogger(__name__)
_LOGGER.setLevel(logging.DEBUG)

# Component registration
CODEOWNER = ["@mnbf9rca"]
DEPENDENCIES = ["m5unified"]
AUTO_LOAD = ["touchscreen"]

# Create namespace and class
m5unified_touch_ns = cg.esphome_ns.namespace("m5unified_touch")
M5UnifiedTouch = m5unified_touch_ns.class_("M5UnifiedTouch", touchscreen.Touchscreen)

# Define configuration schema
CONFIG_SCHEMA = cv.Schema({
    cv.GenerateID(): cv.declare_id(M5UnifiedTouch),
}).extend(touchscreen.TOUCHSCREEN_SCHEMA).extend(cv.COMPONENT_SCHEMA)

async def to_code(config):
    _LOGGER.debug("=== to_code called with config ===")
    try:
        var = cg.new_Pvariable(config[CONF_ID])
        await cg.register_component(var, config)
        await touchscreen.register_touchscreen(var, config)
        return var
    except Exception as e:
        _LOGGER.error(f"Error in to_code: {e}", exc_info=True)
        raise