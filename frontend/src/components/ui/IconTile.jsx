import React from "react";
import { useIntl } from "react-intl";

export default function IconTile({
  icon: Icon,
  bgColor = "#F3F4F6",
  iconColor = "#030213",
}) {
  const intl = useIntl();

  return (
    <div
      className="flex h-10 w-10 items-center justify-center rounded-[10px]"
      style={{ backgroundColor: bgColor }}
      aria-hidden="true"
    >
      <Icon
        className="h-5 w-5"
        style={{ color: iconColor }}
        title={intl.formatMessage({ id: "common.icon" })}
      />
    </div>
  );
}