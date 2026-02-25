import React from "react";
import { useIntl } from "react-intl";
import { Landmark } from "lucide-react";

export default function AppIconBadge({ useRemoteIcon = false, remoteIconSrc }) {
  const intl = useIntl();

  return (
    <div className="h-16 w-16 rounded-2xl bg-[#155dfc] flex items-center justify-center shadow-sm">
      {useRemoteIcon ? (
        <img
          src={remoteIconSrc}
          alt={intl.formatMessage({ id: "appIconBadge.alt" })}
          className="h-8 w-8"
        />
      ) : (
        <Landmark className="h-8 w-8 text-white" aria-hidden="true" />
      )}
    </div>
  );
}