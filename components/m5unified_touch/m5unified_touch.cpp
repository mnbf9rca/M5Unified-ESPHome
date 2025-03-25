#include "m5unified_touch.h"

namespace esphome {
namespace m5unified_touch {

void M5UnifiedTouch::setup() {
  driver_.begin(nullptr);  // Initialize without display for now
}

void M5UnifiedTouch::loop() {
  uint32_t current_time = millis();
  driver_.update(current_time);

  if (driver_.getCount() > 0) {
    const auto& detail = driver_.getDetail(0);
    this->send_touch(detail.x, detail.y);
  } else {
    this->send_release();
  }
}

}  // namespace m5unified_touch
}  // namespace esphome