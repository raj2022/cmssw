// Author
// Seyed Mohsen Etesami setesami@cern.ch

#ifndef PPS_PPSDiamondOrganization_h
#define PPS_PPSDiamondOrganization_h

#include "globals.hh"
#include "SimG4CMS/PPS/interface/PPSVDetectorOrganization.h"
#include "G4Step.hh"

class PPSDiamondOrganization : public PPSVDetectorOrganization {
public:
  PPSDiamondOrganization();
  ~PPSDiamondOrganization() override = default;

  uint32_t GetUnitID(const G4Step* aStep);
  uint32_t GetUnitID(const G4Step* aStep) const override;

private:
  unsigned int theArm;
  unsigned int theStation;
  unsigned int theRoman_pot;
  unsigned int thePlane;
  unsigned int theDetector;
};

#endif  //PPS_PPSDiamondOrganization_h
