import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import touchscreen
from esphome.const import CONF_ID
import logging
import inspect

_LOGGER = logging.getLogger(__name__)
_LOGGER.setLevel(logging.DEBUG)

CODEOWNER = ["@mnbf9rca"]
DEPENDENCIES = ["m5unified"]
AUTO_LOAD = ["touchscreen"]

# Define the component namespace and class
m5unified_touch_ns = cg.esphome_ns.namespace("m5unified_touch")
M5UnifiedTouch = m5unified_touch_ns.class_("M5UnifiedTouch", touchscreen.Touchscreen)

# Define configuration schema
CONFIG_SCHEMA = touchscreen.TOUCHSCREEN_SCHEMA.extend({
    cv.GenerateID(): cv.declare_id(M5UnifiedTouch),
})

async def to_code(config):
    _LOGGER.debug(f"=== to_code called with config ===")
    _LOGGER.debug(f"Config type: {type(config)}")
    _LOGGER.debug(f"Config contents: {config}")
    
    try:
        _LOGGER.debug("Creating variable...")
        var = cg.new_Pvariable(config[CONF_ID])
        _LOGGER.debug(f"Variable created: {var}")

        _LOGGER.debug("Registering touchscreen...")
        await touchscreen.register_touchscreen(var, config)
        _LOGGER.debug(f"Touchscreen registered")
        
        _LOGGER.debug("Registering component...")
        await cg.register_component(var, config)
        _LOGGER.debug("Component registered successfully")
        
        return var
    except Exception as e:
        _LOGGER.error(f"Error in to_code: {e}")
        _LOGGER.error(f"Stack trace:", exc_info=True)
        raise