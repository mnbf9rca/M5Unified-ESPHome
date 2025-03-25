import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import touchscreen
from esphome.const import CONF_ID
import logging

_LOGGER = logging.getLogger(__name__)
_LOGGER.setLevel(logging.DEBUG)

CODEOWNER = ["@mnbf9rca"]
DEPENDENCIES = ["m5unified"]
AUTO_LOAD = ["touchscreen"]

# Debug logging
_LOGGER.debug("Initializing m5unified_touch component")

try:
    m5unified_touch_ns = cg.esphome_ns.namespace("m5unified_touch")
    _LOGGER.debug("Created namespace: m5unified_touch")
    
    M5UnifiedTouch = m5unified_touch_ns.class_("M5UnifiedTouch", touchscreen.Touchscreen)
    _LOGGER.debug("Registered M5UnifiedTouch class")
except Exception as e:
    _LOGGER.error(f"Error during namespace/class registration: {e}")
    raise

CONF_M5UNIFIED_TOUCH_ID = "m5unified_touch_id"

# Debug logging for schema creation
_LOGGER.debug("Creating CONFIG_SCHEMA")

CONFIG_SCHEMA = cv.All(
    touchscreen.TOUCHSCREEN_SCHEMA.extend(
        {
            cv.GenerateID(): cv.declare_id(M5UnifiedTouch),
        }
    ).extend(cv.COMPONENT_SCHEMA),
    cv.only_with_arduino,
)

async def to_code(config):
    _LOGGER.debug(f"to_code called with config: {config}")
    try:
        var = await touchscreen.register_touchscreen(config)
        _LOGGER.debug("Registered touchscreen component")
        await cg.register_component(var, config)
        _LOGGER.debug("Registered base component")
    except Exception as e:
        _LOGGER.error(f"Error in to_code: {e}")
        raise