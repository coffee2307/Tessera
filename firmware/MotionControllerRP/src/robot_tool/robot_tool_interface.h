// --------------------------------------------------------------------------------------
// Project: Tessera
// License: MIT (see LICENSE file for full description)
//          All text in here must be included in any redistribution.
// Maintainer: Tessera project contributors
// --------------------------------------------------------------------------------------

#pragma once

//*** CLASS *****************************************************************************

//--- IRobotTool ------------------------------------------------------------------------

class IRobotTool {
  public:
    virtual ~IRobotTool() {};
    virtual void set_value(float v) = 0;
};
