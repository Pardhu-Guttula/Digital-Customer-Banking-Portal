import React from "react";
import { useIntl } from "react-intl";
import { Landmark } from "lucide-react";

export default function AppIconTile({
  icon: Icon = Landmark,
  "aria-label": ariaLabel,
}) {
  const intl = useIntl();

  return (
    <div
      className="flex items-center justify-center rounded-2xl bg-[#155DFC] w-16 h-16"
      aria-label={ariaLabel ?? intl.formatMessage({ id: "appIconTile.ariaLabel" })}
      role="img"
    >
      <Icon className="h-8 w-8 text-white" aria-hidden="true" />
    </div>
  );
}