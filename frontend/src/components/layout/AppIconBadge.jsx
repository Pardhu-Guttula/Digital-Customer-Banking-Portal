import React from "react";
import { useIntl } from "react-intl";
import { Landmark } from "lucide-react";

export default function AppIconBadge({ useRemoteAsset = false, imgIcon }) {
  const intl = useIntl();

  return (
    <div
      className="grid h-16 w-16 place-items-center rounded-2xl bg-[#155DFC] shadow-sm"
      aria-hidden="true"
      data-label={intl.formatMessage({ id: "appIconBadge.decorative" })}
    >
      {useRemoteAsset ? (
        <img src={imgIcon} alt="" className="block h-8 w-8" />
      ) : (
        <Landmark size={32} color="#FFFFFF" aria-hidden="true" />
      )}
    </div>
  );
}