// --------------------------------------------------------------------------------------
// Project: Tessera
// License: MIT (see LICENSE file for full description)
//          All text in here must be included in any redistribution.
// Maintainer: Tessera project contributors
// --------------------------------------------------------------------------------------

#pragma once

#include "pico/stdlib.h"
#include "hardware/pio.h"
#include "hardware/clocks.h"
#include "robot_tool_interface.h"

//*** CLASS *****************************************************************************

//--- PwmTool ---------------------------------------------------------------------------

class PwmTool : public IRobotTool {
  public:
    ~PwmTool() {};

    void init(int output_pin, int frequency, int resolution_bits);
    void set_value(float v) override;

  private:
    PIO pio = pio0;
    int state_machine = 0;
    int output_pin = 0;

    uint32_t max_pwm = 0;
};
