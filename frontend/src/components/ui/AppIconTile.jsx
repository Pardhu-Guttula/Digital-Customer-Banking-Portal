import React from "react";
import { useIntl } from "react-intl";
import { Landmark } from "lucide-react";

const imgIcon = "https://www.figma.com/api/mcp/asset/447c44d5-7120-4540-959b-8fcd49ec8e78";

export default function AppIconTile({ icon = "lucide", alt }) {
  const intl = useIntl();
  const resolvedAlt = alt ?? intl.formatMessage({ id: "appIconTile.alt" });

  return (
    <div
      className="flex h-16 w-16 items-center justify-center rounded-2xl bg-[#155DFC]"
      aria-label={resolvedAlt}
      role="img"
    >
      {icon === "image" ? (
        <img src={imgIcon} alt={resolvedAlt} className="h-8 w-8" />
      ) : (
        <Landmark className="h-8 w-8 text-white" aria-hidden="true" />
      )}
    </div>
  );
}