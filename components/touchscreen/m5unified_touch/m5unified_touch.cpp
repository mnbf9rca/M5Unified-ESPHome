#include "m5unified_touch_platform.h"
#include "esphome/core/log.h"

namespace esphome {
namespace m5unified_touch {

static const char *TAG = "m5unified_touch";

void M5UnifiedTouchPlatform::setup() {
  ESP_LOGCONFIG(TAG, "Setting up M5Unified Touch Platform...");
  this->m5unified_ = global_m5unified;
}

bool M5UnifiedTouchPlatform::get_touch_data(uint16_t *x, uint16_t *y, bool *touched) {
  if (this->m5unified_ == nullptr || !this->m5unified_->touch.getCount()) {
    *touched = false;
    return true;
  }

  m5::touch_point_t tp;
  if (!this->m5unified_->touch.getDetail(&tp)) {
    *touched = false;
    return true;
  }

  *x = tp.x;
  *y = tp.y;
  *touched = true;
  return true;
}

}  // namespace m5unified_touch
}  // namespace esphome