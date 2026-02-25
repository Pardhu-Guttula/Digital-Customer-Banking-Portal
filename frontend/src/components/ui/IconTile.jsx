import React from "react";
import { useIntl } from "react-intl";

export default function IconTile({ icon: IconComp, bgColor, iconColor, ariaLabel }) {
  const intl = useIntl();
  const resolvedAriaLabel =
    ariaLabel ?? intl.formatMessage({ id: "iconTile.ariaLabel" });

  return (
    <div className="h-[44px] w-[44px] rounded-[10px]" style={{ backgroundColor: bgColor }}>
      <div className="flex h-full w-full items-center justify-center">
        <IconComp
          aria-label={resolvedAriaLabel}
          className="h-[20px] w-[20px]"
          style={{ color: iconColor }}
        />
      </div>
    </div>
  );
}