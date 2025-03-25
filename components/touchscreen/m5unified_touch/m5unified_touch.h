#pragma once

#include "esphome/core/component.h"
#include "esphome/components/touchscreen/touchscreen.h"
#include "../../../m5unified/src/utility/Touch_Class.hpp"

namespace esphome {
namespace m5unified_touch {

class M5UnifiedTouch : public touchscreen::Touchscreen {
 public:
  void setup() override;
  void loop() override;

 protected:
  m5::Touch_Class driver_;
};

}  // namespace m5unified_touch
}  // namespace esphome