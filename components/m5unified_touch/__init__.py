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

def _log_component_info():
    frame = inspect.currentframe()
    caller = inspect.getouterframes(frame)[1]
    _LOGGER.debug(f"Called from: {caller.filename}:{caller.lineno}")
    _LOGGER.debug(f"Available touchscreen components: {dir(touchscreen)}")
    _LOGGER.debug(f"Touchscreen base path: {touchscreen.__file__}")

_LOGGER.debug("=== Starting m5unified_touch initialization ===")
_log_component_info()

try:
    _LOGGER.debug("Creating namespace...")
    assert hasattr(cg, 'esphome_ns'), "esphome_ns not found in codegen"
    m5unified_touch_ns = cg.esphome_ns.namespace("m5unified_touch")
    _LOGGER.debug(f"Namespace created: {m5unified_touch_ns}")
    
    _LOGGER.debug("Creating M5UnifiedTouch class...")
    assert hasattr(touchscreen, 'Touchscreen'), "Touchscreen base class not found"
    M5UnifiedTouch = m5unified_touch_ns.class_("M5UnifiedTouch", touchscreen.Touchscreen)
    _LOGGER.debug(f"M5UnifiedTouch class created: {M5UnifiedTouch}")
    
    # Verify the class was created with correct inheritance
    _LOGGER.debug(f"M5UnifiedTouch parent classes: {M5UnifiedTouch.__bases__ if hasattr(M5UnifiedTouch, '__bases__') else 'No bases found'}")
    
except Exception as e:
    _LOGGER.error(f"Error during initialization: {e}")
    _LOGGER.error(f"Error type: {type(e)}")
    _LOGGER.error(f"Error context: {vars()}")
    raise

CONF_M5UNIFIED_TOUCH_ID = "m5unified_touch_id"

_LOGGER.debug("=== Creating CONFIG_SCHEMA ===")
try:
    assert hasattr(touchscreen, 'TOUCHSCREEN_SCHEMA'), "TOUCHSCREEN_SCHEMA not found"
    CONFIG_SCHEMA = cv.All(
        touchscreen.TOUCHSCREEN_SCHEMA.extend(
            {
                cv.GenerateID(): cv.declare_id(M5UnifiedTouch),
            }
        ).extend(cv.COMPONENT_SCHEMA),
        cv.only_with_arduino,
    )
    _LOGGER.debug(f"CONFIG_SCHEMA created: {CONFIG_SCHEMA}")
except Exception as e:
    _LOGGER.error(f"Error creating CONFIG_SCHEMA: {e}")
    raise

async def to_code(config):
    _LOGGER.debug(f"=== to_code called with config ===")
    _LOGGER.debug(f"Config type: {type(config)}")
    _LOGGER.debug(f"Config contents: {config}")
    
    try:
        _LOGGER.debug("Registering touchscreen...")
        var = await touchscreen.register_touchscreen(config)
        assert var is not None, "register_touchscreen returned None"
        _LOGGER.debug(f"Touchscreen registered: {var}")
        
        _LOGGER.debug("Registering component...")
        await cg.register_component(var, config)
        _LOGGER.debug("Component registered successfully")
        
        return var
    except Exception as e:
        _LOGGER.error(f"Error in to_code: {e}")
        _LOGGER.error(f"Stack trace:", exc_info=True)
        raise