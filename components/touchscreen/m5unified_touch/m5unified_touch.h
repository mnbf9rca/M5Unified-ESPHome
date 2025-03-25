#pragma once

#include "esphome/components/touchscreen/touchscreen.h"
#include "esphome/components/m5unified/m5unified.h"

namespace esphome {
namespace m5unified_touch {

class M5UnifiedTouchPlatform : public touchscreen::TouchScreenPlatform {
 public:
  void setup() override;
  bool get_touch_data(uint16_t *x, uint16_t *y, bool *touched) override;

 protected:
  M5Unified *m5unified_{nullptr};
};

}  // namespace m5unified_touch
}  // namespace esphome