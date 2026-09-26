// --------------------------------------------------------------------------------------
// Project: Tessera
// License: MIT (see LICENSE file for full description)
//          All text in here must be included in any redistribution.
// Maintainer: Tessera project contributors
// --------------------------------------------------------------------------------------

#pragma once

//*** CLASS *****************************************************************************

//--- RobotJoint ------------------------------------------------------------------------

// TODO: create abstract interface for RobotJoint (to support remote Joints)
//       hide direct HW access 

class IRobotJoint {
  public:
    virtual ~IRobotJoint() {};

    void init(int joint_idx);
    void update_target(float p, float v);
    bool load_calibration();
    bool store_calibration();

    virtual bool calibrate(bool print_measurements) = 0;
    virtual void update(float dt, float one_over_dt) = 0;
};

